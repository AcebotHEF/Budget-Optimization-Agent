import pandas as pd

def load_budget_data():
    """
    Creates a dataframe simulating a quarterly budget report 
    with qualitative context for AI analysis.
    """
    data = {
        "Department": [
            "Marketing", 
            "Sales", 
            "Engineering", 
            "HR", 
            "IT Support", 
            "Operations",
            "R&D"
        ],
        "Allocated Budget": [
            80000, 
            60000, 
            150000, 
            40000, 
            50000, 
            70000,
            120000
        ],
        "Actual Spending": [
            95000,  # Over: Aggressive ad campaign
            58000,  # Under: Efficient
            135000, # Under: Delayed hiring
            25000,  # Under: Cancelled training events
            62000,  # Over: Emergency server repairs
            85000,  # Over: Supply chain price hikes
            110000  # Under: Project timeline shift
        ],
        "Strategic Importance (1-10)": [
            9, # Marketing is high priority
            10, # Sales is critical
            10, # Eng is critical
            5, 
            7, 
            8,
            9
        ],
        "Variance Context": [
            "Overspend due to unplanned Q1 product launch ads",
            "Travel costs were lower than expected",
            "Key Senior Dev roles remain unfilled",
            "Q1 training retreat postponed to Q3",
            "Unforeseen hardware failure required replacement",
            "Raw material costs increased by 15%",
            "Prototype testing phase delayed"
        ]
    }
    return pd.DataFrame(data)