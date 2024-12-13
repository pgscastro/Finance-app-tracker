import pandas as pd

class DataAnalyzer:
    def __init__(self):
        pass

    def analyze_by_category(self, transactions):
        if transactions.empty:
            print("No transactions available for analysis.")
            return

        print("--- Total Spending by Category ---")
        category_totals = transactions.groupby("Category")["Amount"].sum()
        print(category_totals)

    def calculate_average_monthly(self, transactions):
        if transactions.empty:
            print("No transactions available for analysis.")
            return

        # Extract the month and year from the Date column
        transactions["Month"] = transactions["Date"].dt.to_period("M")
        monthly_totals = transactions.groupby("Month")["Amount"].sum()
        average_spending = monthly_totals.mean()

        print(f"--- Average Monthly Spending ---")
        print(f"${average_spending:.2f}")

    def show_top_category(self, transactions):
        if transactions.empty:
            print("No transactions available for analysis.")
            return

        category_totals = transactions.groupby("Category")["Amount"].sum()
        top_category = category_totals.idxmax()
        top_spending = category_totals.max()

        print(f"--- Top Spending Category ---")
        print(f"{top_category} with ${top_spending:.2f} total spending.")
