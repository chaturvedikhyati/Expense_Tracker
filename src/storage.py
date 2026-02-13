import pandas as pd
import os

DATA_FILE = "data/expenses.csv"


def initialize_storage():
    """
    Creates the CSV file with headers if it does not exist.
    """
    if not os.path.exists(DATA_FILE):
        df = pd.DataFrame(columns=["date", "category", "amount", "description"])
        df.to_csv(DATA_FILE, index=False)


def load_expenses():
    """
    Loads all expenses from the CSV file.
    Returns a Pandas DataFrame.
    """
    initialize_storage()
    return pd.read_csv(DATA_FILE)


def save_expense(expense: dict):
    """
    Saves a single expense record to the CSV file.
    """
    initialize_storage()
    df = pd.read_csv(DATA_FILE)
    df = pd.concat([df, pd.DataFrame([expense])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)