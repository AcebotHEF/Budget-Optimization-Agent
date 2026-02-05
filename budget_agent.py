from budget_data import load_budget_data
from budget_prompt import budget_template
from langchain.chat_models import ChatOpenAI

def analyze_budget():
    df = load_budget_data()
    table = df.to_string(index=False)

    llm = ChatOpenAI(temperature=0.3)
    prompt = budget_template.format(budget_table=table)
    summary = llm.predict(prompt)

    return df, summary