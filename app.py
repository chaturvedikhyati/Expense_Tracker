import streamlit as st

from src.expense_manager import add_expense
from src.storage import load_expenses
from src.analysis import (
    total_spending,
    category_wise_spending,
    monthly_spending
)
from src.visualization import (
    plot_category_spending,
    plot_monthly_spending
)

st.set_page_config(page_title="Expense Tracker", layout="centered")

st.title("💰 Expense Tracker")

# Sidebar navigation
menu = st.sidebar.radio(
    "Navigation",
    ["Add Expense", "View Expenses", "Analytics"]
)

# ---------------- ADD EXPENSE ----------------
if menu == "Add Expense":
    st.header("➕ Add New Expense")

    date = st.date_input("Date")
    category = st.text_input("Category")
    amount = st.number_input("Amount", min_value=0.01, step=0.01)
    description = st.text_input("Description (optional)")

    if st.button("Add Expense"):
        try:
            add_expense(
                date.strftime("%Y-%m-%d"),
                category,
                float(amount),
                description
            )
            st.success("Expense added successfully!")
        except Exception as e:
            st.error(str(e))

# ---------------- VIEW EXPENSES ----------------
elif menu == "View Expenses":
    st.header("📋 Recorded Expenses")

    df = load_expenses()

    if df.empty:
        st.info("No expenses recorded yet.")
    else:
        st.dataframe(df)

# ---------------- ANALYTICS ----------------
elif menu == "Analytics":
    st.header("📊 Expense Analytics")

    df = load_expenses()

    if df.empty:
        st.warning("No data available for analysis.")
    else:
        # Total spending
        total = total_spending(df)
        st.metric("Total Spending", f"₹ {total:.2f}")

        # Category-wise spending
        st.subheader("Category-wise Spending")
        category_data = category_wise_spending(df)
        st.write(category_data)

        st.pyplot(plot_category_spending(category_data))

        # Monthly trend
        st.subheader("Monthly Spending Trend")
        monthly_data = monthly_spending(df)
        st.write(monthly_data)

        st.pyplot(plot_monthly_spending(monthly_data))