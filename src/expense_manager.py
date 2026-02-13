from datetime import datetime
from src.storage import save_expense


def validate_date(date_str: str) -> str:
    """
    Validates and formats date input.
    Expected format: YYYY-MM-DD
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")


def validate_amount(amount: float) -> float:
    """
    Ensures amount is a positive number.
    """
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
    return round(amount, 2)


def validate_category(category: str) -> str:
    """
    Validates category input.
    """
    if not category.strip():
        raise ValueError("Category cannot be empty")
    return category.strip().title()


def add_expense(date, category, amount, description=""):
    """
    Main function to add an expense.
    """
    expense = {
        "date": validate_date(date),
        "category": validate_category(category),
        "amount": validate_amount(amount),
        "description": description.strip()
    }

    save_expense(expense)