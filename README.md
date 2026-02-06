# 📊 Budget Optimization & FP&A AI Agent

**A strategic financial planning tool powered by OpenAI and LangChain.**



## 📌 Overview
The **Budget Optimization Agent** is an AI-powered dashboard designed to assist Financial Planning & Analysis (FP&A) teams. Unlike standard Excel reports, this tool doesn't just track spending—it understands **strategic context**.

It ingests department-level budget data (including "Strategic Importance" scores and variance reasons) and uses **OpenAI (GPT-3.5/4)** to recommend intelligent budget reallocations.

## 🚀 Features
* **Smart Variance Analysis:** Detects overspending and determines if it was "Wasteful" or "Critical" based on qualitative context.
* **Strategic Reallocation:** The AI protects high-priority departments (e.g., Engineering, Sales) while recommending cuts in low-impact areas.
* **Interactive Visualization:** Features a side-by-side **Matplotlib** bar chart to visually compare Allocated Budget vs. Actual Spending.
* **Executive Reporting:** Generates a professional, bulleted strategy memo suitable for CFO review.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **AI Orchestration:** LangChain (Core & OpenAI)
* **LLM:** OpenAI GPT-3.5 Turbo (or GPT-4)
* **Data Visualization:** Matplotlib & NumPy
* **Data Handling:** Pandas
* **Environment:** Python 3.10+

## 📂 Project Structure
```text
budget_agent/
├── budget_app.py       # Main Dashboard (Streamlit + Charts)
├── budget_agent.py     # AI Logic (LangChain + OpenAI connection)
├── budget_data.py      # Data Generator (Includes Strategic Scores)
├── budget_prompt.py    # "FP&A Manager" Persona Prompt
├── requirements.txt    # Dependencies
├── .env                # API Keys (Not tracked in git)
└── README.md           # Documentation
⚙️ Setup & Installation
1. Clone the Repository
Bash
git clone [https://github.com/yourusername/budget-optimization-agent.git](https://github.com/yourusername/budget-optimization-agent.git)
cd budget-optimization-agent
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Configure API Keys
Create a file named .env in the root folder and add your OpenAI API key:

Ini, TOML
OPENAI_API_KEY=sk-proj-....................
4. Run the Application
Launch the dashboard locally:

Bash
python -m streamlit run budget_app.py
