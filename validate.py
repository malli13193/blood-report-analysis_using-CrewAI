#!/usr/bin/env python3
"""
Validation script to verify the enhanced CrewAI system structure
"""

import os
import sys
from pdf_to_text import pdf_to_text

def validate_system():
    """Validate the three-agent system setup"""
    print("🔍 Validating Enhanced CrewAI Blood Report Analysis System")
    print("=" * 60)
    
    checks = []
    
    # Check 1: Required files exist
    required_files = [
        'main.py',
        'pdf_to_text.py', 
        'requirements.txt',
        '.env',
        'data/blood_Report_Sample.pdf'
    ]
    
    print("\n📁 Checking required files...")
    for file in required_files:
        exists = os.path.exists(file)
        status = "✅" if exists else "❌"
        print(f"   {status} {file}")
        checks.append(exists)
    
    # Check 2: Verify agent count in main.py
    print(f"\n🤖 Checking agents in main.py...")
    try:
        with open('main.py', 'r') as f:
            content = f.read()
            
        agent_count = content.count('Agent(')
        task_count = content.count('Task(')
        
        print(f"   ✅ Found {agent_count} agents")
        print(f"   ✅ Found {task_count} tasks")
        
        # Check for specific agents
        agents_found = {
            'Blood_report_analyst': 'Blood_report_analyst= Agent(' in content,
            'Health_blogger': 'Experienced_health_blogger = Agent(' in content,
            'Medical_doctor': 'Medical_doctor = Agent(' in content
        }
        
        for agent_name, found in agents_found.items():
            status = "✅" if found else "❌"
            print(f"   {status} {agent_name}")
            checks.append(found)
            
    except Exception as e:
        print(f"   ❌ Error reading main.py: {e}")
        checks.append(False)
    
    # Check 3: Test PDF conversion
    print(f"\n📄 Testing PDF to text conversion...")
    try:
        pdf_path = './data/blood_Report_Sample.pdf'
        txt_path = './data/test_conversion.txt'
        
        if os.path.exists(pdf_path):
            pdf_to_text(pdf_path, txt_path)
            if os.path.exists(txt_path):
                print("   ✅ PDF conversion successful")
                # Clean up test file
                os.remove(txt_path)
                checks.append(True)
            else:
                print("   ❌ PDF conversion failed - no output file")
                checks.append(False)
        else:
            print("   ❌ PDF file not found")
            checks.append(False)
    except Exception as e:
        print(f"   ❌ PDF conversion error: {e}")
        checks.append(False)
    
    # Summary
    passed = sum(checks)
    total = len(checks)
    
    print(f"\n📊 Validation Summary:")
    print(f"   Passed: {passed}/{total} checks")
    
    if passed == total:
        print("   🎉 All checks passed! System is ready.")
        print(f"\n🚀 Next steps:")
        print("   1. Add your API keys to .env file")
        print("   2. Run: python main.py")
        return True
    else:
        print("   ⚠️  Some checks failed. Please review the issues above.")
        return False

if __name__ == "__main__":
    success = validate_system()
    sys.exit(0 if success else 1)