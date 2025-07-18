# Project Setup and Execution Guide



# 🧠 Blood Report Analysis System using CrewAI

## 📌 Overview

This project is a generative AI system that automates the analysis of blood reports using **CrewAI**. It employs a multi-agent architecture where one agent extracts key health metrics from a PDF blood report, and another provides actionable health recommendations using external resources.

Built as part of the **Wingify Software Pvt. Ltd. – AI Intern Debug Challenge**, this project demonstrates problem-solving, debugging, and integration skills using advanced AI tools.

🔗 **Live Repo**: [https://github.com/malli13193/blood-report-analysis_using-CrewAI](https://github.com/malli13193/blood-report-analysis_using-CrewAI)

---

## 🚀 How It Works

### 📥 Input:
- PDF Blood Report (e.g., `blood_Report_Sample.pdf`)

### ⚙️ Flow:
1. **Convert PDF to Text** using `PyMuPDF`
2. **Agent 1: Blood Report Analyst**
   - Summarizes critical medical data like Hemoglobin, RBC count, etc.
3. **Agent 2: Health Blogger**
   - Searches medical sources and gives health recommendations
4. **Output:**
   - JSON file with recommendations and reference URLs

![Flow Diagram](flow_diagram.png)

---

## 🛠️ Tools & Technologies

| Tool/Library       | Purpose                                 |
|--------------------|------------------------------------------|
| Python 3.11        | Latest runtime                          |
| [CrewAI](https://docs.crewai.com)        | Multi-agent framework                  |
| `crewai_tools`     | Agent tools: File, Web, PDF Reader       |
| `pymupdf` (fitz)   | PDF to text conversion                   |
| OpenAI API         | LLM for text generation (`gpt-3.5-turbo`)|
| `.env`             | API key management                       |

---

## ⚠️ Debugging & Fixes

### ❌ Original Issues:
- Typo: `requirement.txt` → `requirements.txt`
- Dependency Conflict:
  - `crewai==0.121.1` requires `chromadb>=0.5.23`
  - `crewai-tools==0.1.0` requires `chromadb<0.5.0`

### ✅ Fixes Applied:
- Used only:
  ```txt
  crewai
  crewai_tools
  pymupdf


* Removed `chromadb` entirely
* Merged multiple files (`task.py`, `tool.py`, etc.) into a single `main.py` for easier debugging
* Added `.env` support with OpenAI key
* Switched to a new OpenAI account to resolve API quota errors


## 🧪 Sample Output

You can view the final output file `output.json` and visual summary:

![Output Sample 1](output1.png)
![Output Sample 2](output2.png)
![Output Sample 3](output3.png)

---

## 💡 Future Work (If Time Permits)

If given the opportunity or more time, the following enhancements are planned:

* **Queue Worker Model**:

  * Add Redis Queue or Celery for handling concurrent requests
* **Database Integration**:

  * Store user info and report summaries in PostgreSQL
* **Frontend Interface**:

  * Use **Streamlit** to deploy the app for real-time report uploads and analysis
* **Improved PDF Parsing**:

  * Use table-aware models to extract better horizontal data layout



## 📋 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/malli13193/blood-report-analysis_using-CrewAI.git
cd blood-report-analysis_using-CrewAI
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Add your `.env` file

```env
OPENAI_API_KEY=your_openai_key
```

### 5. Run the main application

```bash
python main.py
```


## 👨‍💻 Author

**K Mallikarjuna Reddy**
Role Applied: Intern - Generative AI at Wingify
Contact: [mallikarjunareddykanala2003@gmail.com](mailto:mallikarjunareddykanala2003@gmail.com)

---

## 📜 License

This project is intended for learning.
