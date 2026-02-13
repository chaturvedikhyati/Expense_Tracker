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


def show_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Category-wise Analysis")
    print("5. Monthly Spending Trend")
    print("6. Exit")


def handle_add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description (optional): ")

        add_expense(date, category, amount, description)
        print("✅ Expense added successfully!")

    except ValueError as e:
        print(f"❌ Error: {e}")


def handle_view_expenses():
    df = load_expenses()
    if df.empty:
        print("No expenses recorded yet.")
    else:
        print("\nRecorded Expenses:")
        print(df.to_string(index=False))


def handle_total_spending():
    df = load_expenses()
    if df.empty:
        print("No data available.")
        return

    total = total_spending(df)
    print(f"\n💰 Total Spending: ₹{total:.2f}")


def handle_category_analysis():
    df = load_expenses()
    if df.empty:
        print("No data available.")
        return

    category_data = category_wise_spending(df)
    print("\nCategory-wise Spending:")
    print(category_data)
    plot_category_spending(category_data)


def handle_monthly_trend():
    df = load_expenses()
    if df.empty:
        print("No data available.")
        return

    monthly_data = monthly_spending(df)
    print("\nMonthly Spending:")
    print(monthly_data)
    plot_monthly_spending(monthly_data)


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            handle_add_expense()
        elif choice == "2":
            handle_view_expenses()
        elif choice == "3":
            handle_total_spending()
        elif choice == "4":
            handle_category_analysis()
        elif choice == "5":
            handle_monthly_trend()
        elif choice == "6":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()