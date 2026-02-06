import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
# Ensure budget_agent.py is in the same folder
from budget_agent import analyze_budget

# 1. Page Config for a wider, dashboard-like view
st.set_page_config(page_title="Budget Optimization", layout="wide", page_icon="📊")

st.title("📊 Budget Optimization Agent")
st.markdown("### AI-Powered FP&A Dashboard")

# 2. Main Action Button
if st.button("Run Strategic Analysis", type="primary"):
    
    with st.spinner("Crunching the numbers and consulting the AI..."):
        # Call the agent
        df, result = analyze_budget()

        if df is not None:
            # --- ROW 1: Data & Visualization ---
            col1, col2 = st.columns([1, 1.5])

            with col1:
                st.subheader("💵 Q1 Financial Data")
                # Highlight variances: Red text isn't easy in standard st.dataframe without pandas styling, 
                # but we can show the raw data cleanly.
                st.dataframe(df, use_container_width=True, height=400)

            with col2:
                st.subheader("📈 Budget vs. Actual")
                
                # --- Improved Side-by-Side Bar Chart ---
                departments = df["Department"]
                x = np.arange(len(departments))  # Label locations
                width = 0.35  # Width of the bars

                fig, ax = plt.subplots(figsize=(8, 5))
                rects1 = ax.bar(x - width/2, df["Allocated Budget"], width, label='Budget', color='#4c72b0')
                rects2 = ax.bar(x + width/2, df["Actual Spending"], width, label='Actual', color='#dd8452')

                # Add text for labels, title and custom x-axis tick labels, etc.
                ax.set_ylabel('USD ($)')
                ax.set_title('Budget Allocation vs. Actual Spending')
                ax.set_xticks(x)
                ax.set_xticklabels(departments, rotation=45, ha="right")
                ax.legend()
                
                # Add a grid for easier reading
                ax.yaxis.grid(True, linestyle='--', alpha=0.7)

                st.pyplot(fig)

            # --- ROW 2: AI Report ---
            st.divider()
            st.subheader("🧠 Strategic AI Recommendations")
            st.markdown(result)
            
        else:
            st.error(result) # Show error if agent failed