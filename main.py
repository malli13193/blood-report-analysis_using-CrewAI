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
docs_tool = DirectoryReadTool(directory=r'C:\Users\bhanu\Desktop\CREWAI-powered-Blood-Report-Analysis-main\data')
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
    output_file=r'C:\Users\bhanu\Desktop\CREWAI-powered-Blood-Report-Analysis-main\output.json'
)

# Assemble a crew
crew = Crew(
    agents=[Blood_report_analyst, Experienced_health_blogger],
    tasks=[analyse_blood_report_task, generate_feedback_and_URLs],
    verbose=True
)
pdf_path = r'C:\Users\bhanu\Desktop\CREWAI-powered-Blood-Report-Analysis-main\data\blood_Report_Sample.pdf'
txt_path = os.path.splitext(pdf_path)[0] + ".txt"

pdf_to_text(pdf_path, txt_path)

# pdf_to_text("source of your pdf","destination of your text file")

inputs = {
    'topic': 'Blood Reports and Health',
    'text_file' : txt_path

}
# Execute tasks
crew.kickoff(inputs=inputs)


