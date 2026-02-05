import pandas as pd

def load_budget_data():
    data = {
        "Department": ["Marketing", "Sales", "Engineering", "HR", "IT", "Operations"],
        "Allocated Budget": [80000, 60000, 150000, 40000, 50000, 70000],
        "Actual Spending": [95000, 58000, 140000, 30000, 60000, 85000]
    }
    return pd.DataFrame(data)