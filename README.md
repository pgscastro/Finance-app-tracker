# Personal Finance Tracker App

## 📋 Description
The **Personal Finance Tracker App** is a Python application designed to help users manage their personal finances effectively. With features to import, view, edit, analyze, and visualize transaction data, the app simplifies the process of tracking and understanding spending habits. Using powerful Python libraries like `pandas` and `matplotlib`.

---

## 🚀 Installation

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd personal-finance-tracker
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

1. Start the application by running the following command:
   ```bash
   python menu.py
   ```
2. Follow the menu-driven interface to:
   - Import transaction data.
   - View and manage transactions.
   - Analyze and visualize spending patterns.

---

## ✨ Features

### File Management
- Import a CSV file containing transaction data (columns: Date, Category, Description, Amount).
- Save updated transactions to a CSV file for future reference.

### Data Management
- View all transactions or filter them by a specific date range.
- Add new transactions with details like date, category, description, and amount.
- Edit or delete existing transactions interactively.

### Spending Analysis
- Analyze spending by category to see where money is going.
- Calculate average monthly spending for a clearer financial overview.
- Identify the category with the highest spending.

### Data Visualization
- **Line Chart**: Visualize monthly spending trends.
- **Bar Chart**: Compare spending across categories.
- **Pie Chart**: View percentage distribution of spending by category.

---

## 📊 Example Output

### Spending Analysis Example:
```
--- Total Spending by Category ---
Food             $1,200.50
Rent             $2,000.00
Utilities          $300.75
...

--- Average Monthly Spending ---
$1,450.75

--- Top Spending Category ---
Rent with $2,000.00 total spending.
```

### Visualizations:
- A line chart showing monthly spending trends.
- A bar chart displaying spending by category.
- A pie chart illustrating percentage distribution.

---

## 🛠️ Built With
- **Python**: Core programming language.
- **pandas**: Data manipulation and analysis.
- **matplotlib**: Visualization library.
- **seaborn**: Enhanced data visualization.

---

## 📝 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📩 Contact
- **Author**: Pedro Schdmidt
- **Email**: pgscastro@gmail.com
