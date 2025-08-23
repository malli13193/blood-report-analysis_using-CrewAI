#!/usr/bin/env python3
"""
Test script to demonstrate the enhanced CrewAI blood report analysis system
with three agents (persons): Blood Report Analyst, Health Advisor, and Medical Doctor.

This script shows the structure and workflow without requiring API keys.
"""

import os
from pdf_to_text import pdf_to_text

def demo_three_agent_system():
    """
    Demonstrates the three-agent CrewAI system structure
    """
    print("🧠 Blood Report Analysis System using CrewAI")
    print("=" * 50)
    print("\n📋 Current System Configuration:")
    
    # Show the three agents
    agents = [
        {
            "name": "Blood Report Analyst",
            "role": "Analyzes blood test reports and summarizes key health indicators",
            "tools": ["FileReadTool", "PDFSearchTool", "DirectoryReadTool"]
        },
        {
            "name": "Health Advisor", 
            "role": "Provides health recommendations based on analysis and web research",
            "tools": ["SerperDevTool", "WebsiteSearchTool", "DirectoryReadTool", "FileReadTool"]
        },
        {
            "name": "Medical Doctor",
            "role": "Provides professional medical interpretation and clinical insights",
            "tools": ["FileReadTool", "DirectoryReadTool"]
        }
    ]
    
    print(f"\n👥 Active Agents: {len(agents)}")
    for i, agent in enumerate(agents, 1):
        print(f"\n{i}. **{agent['name']}**")
        print(f"   Role: {agent['role']}")
        print(f"   Tools: {', '.join(agent['tools'])}")
    
    # Show the workflow
    print(f"\n🔄 Workflow:")
    print("1. 📄 Convert PDF blood report to text")
    print("2. 🔍 Blood Report Analyst analyzes the report")
    print("3. 💡 Health Advisor provides recommendations")
    print("4. 🩺 Medical Doctor reviews and validates findings")
    print("5. 📤 Generate comprehensive output files")
    
    # Test PDF conversion
    print(f"\n🧪 Testing PDF to Text Conversion...")
    pdf_path = './data/blood_Report_Sample.pdf'
    txt_path = './data/blood_Report_Sample.txt'
    
    if os.path.exists(pdf_path):
        pdf_to_text(pdf_path, txt_path)
        print("✅ PDF successfully converted to text")
        
        # Show sample extracted text
        with open(txt_path, 'r') as f:
            sample_text = f.read()[:200]
            print(f"\n📝 Sample extracted text:")
            print("-" * 30)
            print(sample_text + "...")
            print("-" * 30)
    else:
        print("❌ PDF file not found")
    
    # Show output files that would be generated
    print(f"\n📁 Expected Output Files:")
    print("1. output.json - Health recommendations with URLs")
    print("2. medical_review.json - Professional medical review")
    
    print(f"\n🎉 System ready! To run with API keys:")
    print("1. Add your OpenAI API key to .env file")
    print("2. Add your Serper API key to .env file") 
    print("3. Run: python main.py")

if __name__ == "__main__":
    demo_three_agent_system()