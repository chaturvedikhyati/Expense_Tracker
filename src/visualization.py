import matplotlib.pyplot as plt
import pandas as pd


def plot_category_spending(category_data: pd.Series):
    fig, ax = plt.subplots()
    category_data.plot(kind="bar", ax=ax)
    ax.set_title("Category-wise Spending")
    ax.set_xlabel("Category")
    ax.set_ylabel("Amount Spent")
    plt.tight_layout()
    return fig


def plot_monthly_spending(monthly_data: pd.Series):
    fig, ax = plt.subplots()
    monthly_data.sort_index().plot(marker="o", ax=ax)
    ax.set_title("Monthly Spending Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount Spent")
    ax.grid(True)
    plt.tight_layout()
    return fig