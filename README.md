💰 Expense Tracker System (Python)

A simple yet efficient Expense Tracker System built using Python.
This project helps users manage, analyze, and monitor their daily expenses with an easy-to-use console-based interface.

🧩 Features

Add Expenses: Record daily expenses with date, description, and amount.

View Expenses: Display all stored expenses in a neatly formatted table using tabulate.

Delete Expenses: Remove a specific expense entry by index, with automatic reindexing.

Search Expenses: Find expenses by description keyword.

Sort Expenses: Sort the list of expenses in ascending or descending order by amount.

Monthly Totals: View expenses for a specific month and year with selective_total().

CSV Storage: All data is stored in expenses.csv, allowing easy viewing and portability.

🗂️ File Structure
ExpenseTracker/
│
├── expense_tracker.py     # Main Python script (class-based implementation)
├── expenses.csv            # CSV file storing all expenses
└── README.md               # Project documentation

⚙️ Technologies Used

Python 3

Tabulate (for table formatting)

CSV file handling

OS module (for file checking and path handling)

🚀 Future Enhancements

Add category-wise expense summaries

Include visualization (e.g., bar chart for monthly spending)

Integrate a simple GUI (Tkinter / PyQt)

Export data to Excel or PDF reports

Set budget limits and get alerts

🧠 Learning Objectives

This project demonstrates:

File handling (read/write operations)

Data organization and reindexing

User input validation

Basic data analysis with Python
