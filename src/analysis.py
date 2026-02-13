import pandas as pd


def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts date column to datetime and adds month column.
    """
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")
    return df


def total_spending(df: pd.DataFrame) -> float:
    """
    Returns total spending amount.
    """
    return df["amount"].sum()


def category_wise_spending(df: pd.DataFrame) -> pd.Series:
    """
    Returns total spending per category.
    """
    return df.groupby("category")["amount"].sum().sort_values(ascending=False)


def monthly_spending(df: pd.DataFrame) -> pd.Series:
    """
    Returns monthly spending summary.
    """
    df = prepare_data(df)
    return df.groupby("month")["amount"].sum()