from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from budget_data import load_budget_data
from budget_prompt import budget_template

# Load API Key (OPENAI_API_KEY)
load_dotenv()

def analyze_budget():
    """
    Loads budget data and uses OpenAI GPT to generate a strategic analysis.
    """
    try:
        # 1. Load the Data
        df = load_budget_data()
        
        # Convert to string for the AI
        table = df.to_string(index=False)

        # 2. Initialize OpenAI
        # 'gpt-3.5-turbo' is standard. Use 'gpt-4' if you have access and want smarter analysis.
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)

        # 3. Create the Chain
        chain = budget_template | llm

        # 4. Invoke the chain
        response = chain.invoke({"budget_table": table})

        # Return the DataFrame and the AI's response text
        return df, response.content

    except Exception as e:
        return None, f"Error generating budget analysis: {e}"