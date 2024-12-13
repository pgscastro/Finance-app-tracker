import matplotlib.pyplot as plt
import pandas as pd

class Visualizer:
    def __init__(self):
        pass

    def visualize_monthly_trend(self, transactions):
        if transactions.empty:
            print("No transactions available for visualization.")
            return

        transactions["Month"] = transactions["Date"].dt.to_period("M")
        monthly_totals = transactions.groupby("Month")["Amount"].sum()

        plt.figure(figsize=(10, 6))
        monthly_totals.plot(kind="line", marker="o")
        plt.title("Monthly Spending Trend")
        plt.xlabel("Month")
        plt.ylabel("Total Spending ($)")
        plt.grid()
        plt.show()

    def visualize_spending_by_category(self, transactions):
        if transactions.empty:
            print("No transactions available for visualization.")
            return

        category_totals = transactions.groupby("Category")["Amount"].sum()

        plt.figure(figsize=(10, 6))
        category_totals.plot(kind="bar")
        plt.title("Spending by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Spending ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def visualize_spending_distribution(self, transactions):
        if transactions.empty:
            print("No transactions available for visualization.")
            return

        category_totals = transactions.groupby("Category")["Amount"].sum()

        plt.figure(figsize=(8, 8))
        category_totals.plot(kind="pie", autopct="%1.1f%%", startangle=140)
        plt.title("Spending Distribution by Category")
        plt.ylabel("")  # Remove the default y-axis label
        plt.tight_layout()
        plt.show()
