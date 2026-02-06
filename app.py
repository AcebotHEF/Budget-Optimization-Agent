import streamlit as st
import matplotlib.pyplot as plt
from budget_agent import analyze_budget

st.title("📊 Budget Optimization Agent")

if st.button("Analyze Budget"):
    df, result = analyze_budget()

    st.subheader("💵 Budget Overview")
    st.dataframe(df)

    st.subheader("📈 Budget Performance Chart")
    fig, ax = plt.subplots()
    ax.bar(df["Department"], df["Allocated Budget"], label="Budget", alpha=0.6)
    ax.bar(df["Department"], df["Actual Spending"], label="Spent", alpha=0.6)
    ax.set_ylabel("USD")
    ax.legend()
    st.pyplot(fig)

    st.subheader("🧠 AI Recommendations")
    st.write(result)