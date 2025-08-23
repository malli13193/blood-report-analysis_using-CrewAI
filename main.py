import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from pdf_to_text import pdf_to_text
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool,
    PDFSearchTool
)

load_dotenv()
####docs tool is for the output directory used by last agent in the sequence 
# Set up API keys
# os.environ["SERPER_API_KEY"] = "SERPER_API_KEY" 
# os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"
# os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"
# Instantiate tools
docs_tool = DirectoryReadTool(directory='./data')
file_tool = FileReadTool() #added as failsafe
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()
pdf_read_tool= PDFSearchTool()

# Create agents
Blood_report_analyst= Agent(
    role= 'Blood Report Analyst',
    goal= 'Analyze the given blood test report and summarize key points',
    backstory= 'You are a proficient analyst with extensive experience in interpreting blood test results . Your ability to identify crucial health indicators and summarize findings helps in delivering actionable insights.',
    tools=[file_tool,pdf_read_tool, docs_tool],
    #model="gpt-3.5-turbo",
    allow_delegation=False,
    verbose=True
)

Experienced_health_blogger = Agent(
    role= 'Health Advisor',
    goal = 'Provide health recommendations based on the summary provided by the blood report analyst and related articles found on the internet ',
    backstory = 'You are a knowledgeable health advisor who integrates medical data and internet article findings to offer practical health recommendations. Your advice helps individuals make informed decisions about their health.Also, you will always provide the source URL from which you are using any and all information, always cite souces',
    tools=[search_tool, web_rag_tool,docs_tool,file_tool],
    #model="gpt-3.5-turbo",
    allow_delegation=False,
    verbose=True
)

# Adding a third agent - Medical Doctor
Medical_doctor = Agent(
    role='Medical Doctor',
    goal='Provide professional medical interpretation and clinical insights based on blood test results and health recommendations',
    backstory='You are an experienced medical doctor with expertise in laboratory medicine and internal medicine. You can interpret complex blood test results, identify potential medical conditions, suggest follow-up tests, and provide clinical context for health recommendations. You focus on medical accuracy and safety.',
    tools=[file_tool, docs_tool],
    #model="gpt-3.5-turbo", 
    allow_delegation=False,
    verbose=True
)

# Define tasks
analyse_blood_report_task = Task(
    description='The Blood Report Analyst will analyze the blood test report  provided in the input file. The analysis will focus on summarizing key health indicators and findings from the blood test.',
    expected_output='The output will be a JSON file containing a summarized report of the key points identified in the blood test.',
    agent=Blood_report_analyst
)

generate_feedback_and_URLs = Task(
    description='The Experienced health blogger will provide health recommendations based on the findings of the blood report analyst . This will include informaton from related articles and their URLs. providing their URLs is absolutely necessary ',
    expected_output='The output will be a JSON file containing detailed health recommendations along with the URLs of the articles from which these recommendations are based off of.',
    agent= Experienced_health_blogger,
    context=[analyse_blood_report_task],
    output_file='./output.json'
)

# Adding a new task for the Medical Doctor
medical_review_task = Task(
    description='The Medical Doctor will review the blood test analysis and health recommendations to provide professional medical insights, identify any potential medical conditions or concerns, suggest appropriate follow-up actions, and validate the safety of the recommendations.',
    expected_output='The output will be a JSON file containing professional medical review, clinical interpretations, potential diagnoses, recommended follow-up tests or consultations, and medical validation of the health advice.',
    agent=Medical_doctor,
    context=[analyse_blood_report_task, generate_feedback_and_URLs],
    output_file='./medical_review.json'
)

# Assemble a crew
crew = Crew(
    agents=[Blood_report_analyst, Experienced_health_blogger, Medical_doctor],
    tasks=[analyse_blood_report_task, generate_feedback_and_URLs, medical_review_task],
    verbose=True
)
pdf_path = './data/blood_Report_Sample.pdf'
txt_path = os.path.splitext(pdf_path)[0] + ".txt"

pdf_to_text(pdf_path, txt_path)

# pdf_to_text("source of your pdf","destination of your text file")

inputs = {
    'topic': 'Blood Reports and Health',
    'text_file' : txt_path

}
# Execute tasks
crew.kickoff(inputs=inputs)


