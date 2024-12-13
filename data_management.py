import pandas as pd


class DataManager:
    def __init__(self):
        self.transactions = pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])

    def import_file(self):
        try:
            file_path = input("Enter the file path to the CSV file: ")
            df = pd.read_csv(file_path)

            required_columns = {"Date", "Category", "Description", "Amount"}
            if not required_columns.issubset(df.columns):
                print("Error: CSV file must contain the following columns: Date, Category, Description, Amount.")
                return

            df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
            df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

            if df["Date"].isnull().any() or df["Amount"].isnull().any():
                print("Error: Some rows have invalid dates or amounts.")
                return

            self.transactions = df
            print("File imported successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def view_all(self):
        if self.transactions.empty:
            print("No transactions found. Please import a file first.")
        else:
            print("--- All Transactions ---")
            print(self.transactions)

    def view_by_date_range(self):
        if self.transactions.empty:
            print("No transactions found. Please import a file first.")
            return

        try:
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")
            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)

            filtered = self.transactions[
                (self.transactions["Date"] >= start_date) & (self.transactions["Date"] <= end_date)
                ]

            if filtered.empty:
                print("No transactions found in this date range.")
            else:
                print("--- Transactions from", start_date.date(), "to", end_date.date(), "---")
                print(filtered)
        except Exception as e:
            print(f"Error: {e}")

    def add_transaction(self):
        try:
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            description = input("Enter a description: ")
            amount = float(input("Enter the amount: "))

            new_transaction = {"Date": pd.to_datetime(date), "Category": category, "Description": description,
                               "Amount": amount}
            self.transactions = pd.concat([self.transactions, pd.DataFrame([new_transaction])], ignore_index=True)
            print("Transaction added successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def edit_transaction(self):
        if self.transactions.empty:
            print("No transactions found. Please import a file first.")
            return

        try:
            index = int(input("Enter the index of the transaction to edit: "))
            if index < 0 or index >= len(self.transactions):
                print("Invalid index.")
                return

            print("Current Transaction Details:")
            print(self.transactions.loc[index])

            date = input("Enter new date (YYYY-MM-DD) or press Enter to keep current: ")
            category = input("Enter new category or press Enter to keep current: ")
            description = input("Enter new description or press Enter to keep current: ")
            amount = input("Enter new amount or press Enter to keep current: ")

            if date:
                self.transactions.at[index, "Date"] = pd.to_datetime(date)
            if category:
                self.transactions.at[index, "Category"] = category
            if description:
                self.transactions.at[index, "Description"] = description
            if amount:
                self.transactions.at[index, "Amount"] = float(amount)

            print("Transaction updated successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def delete_transaction(self):
        if self.transactions.empty:
            print("No transactions found. Please import a file first.")
            return

        try:
            index = int(input("Enter the index of the transaction to delete: "))
            if index < 0 or index >= len(self.transactions):
                print("Invalid index.")
                return

            self.transactions = self.transactions.drop(index).reset_index(drop=True)
            print("Transaction deleted successfully!")
        except Exception as e:
            print(f"Error: {e}")
