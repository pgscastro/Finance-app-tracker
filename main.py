from data_management import DataManager
from data_analysis import DataAnalyzer
from visualization import Visualizer

def main():
    manager = DataManager()
    analyzer = DataAnalyzer()
    visualizer = Visualizer()

    while True:
        print("""
        === Personal Finance Tracker ===
        0. Import a CSV File
        1. View All Transactions
        2. View Transactions by Date Range
        3. Add a Transaction
        4. Edit a Transaction
        5. Delete a Transaction
        6. Analyze Spending by Category
        7. Calculate Average Monthly Spending
        8. Show Top Spending Category
        9. Visualize Monthly Spending Trend
        10. Visualize Spending by Category
        11. Visualize Spending Distribution
        12. Exit
        """)
        choice = input("Choose an option (0-12): ")

        if choice == '0':
            manager.import_file()
        elif choice == '1':
            manager.view_all()
        elif choice == '2':
            manager.view_by_date_range()
        elif choice == '3':
            manager.add_transaction()
        elif choice == '4':
            manager.edit_transaction()
        elif choice == '5':
            manager.delete_transaction()
        elif choice == '6':
            analyzer.analyze_by_category(manager.transactions)
        elif choice == '7':
            analyzer.calculate_average_monthly(manager.transactions)
        elif choice == '8':
            analyzer.show_top_category(manager.transactions)
        elif choice == '9':
            visualizer.visualize_monthly_trend(manager.transactions)
        elif choice == '10':
            visualizer.visualize_spending_by_category(manager.transactions)
        elif choice == '11':
            visualizer.visualize_spending_distribution(manager.transactions)
        elif choice == '12':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
