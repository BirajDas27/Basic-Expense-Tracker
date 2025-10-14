# 💸 Expense Tracker System (Python)

A **simple and efficient console-based Expense Tracker** built with Python.  
Easily record, view, and manage your daily expenses while keeping your budget in check.  
Perfect for beginners learning file handling and Python basics!

---

## ✨ Features

✅ **Add Expense** — Record date, description, and amount easily  
📋 **View Expense** — Display all expenses in a clean table using `tabulate`  
🔍 **Search Expense** — Find expenses by description keywords  
🗑️ **Delete Expense** — Remove a specific record and auto-update indexes  
💰 **Sort Expenses** — Sort records in ascending or descending order of amount  
📆 **Monthly Totals** — View expenses for a selected month and year  
💾 **CSV Data Storage** — All records are saved in `expenses.csv` for easy access  

---

## 📂 Project Structure

ExpenseTracker/
│
├── expense_tracker.py # Main program file
├── expenses.csv # Stores all expense data
└── README.md # Project documentation

---

## ⚙️ Technologies Used

- 🐍 **Python 3**
- 📊 **Tabulate Library** (for clean tabular display)
- 🧱 **CSV File Handling**
- 🧩 **OS Module** (for file management and checks)

---

## 🧠 Concepts Covered

- File handling (`read`, `write`, `append`, `delete`)
- Data parsing and reindexing
- List and string manipulation
- CLI-based user interaction
- Basic data organization and filtering

---

## 🚀 How to Run

1. Clone this repository  
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker

---

## 📚 Packages

Tabulate package - pip install tabulate

---

## 🧮 Run the program

python expense_tracker.py

---

## 🎯 Some important features

* Add new expenses
* View all records
* Search or delete entries
* Check monthly totals

---

🌟 Example Output

+--------+------------+---------------+----------+
| Index  | Date       | Description   | Amount   |
+--------+------------+---------------+----------+
| 1      | 2023-01-02 | grocery       | 3000.0   |
| 2      | 2023-01-05 | netflix       | 499.0    |
| 3      | 2023-01-20 | travel        | 10000.0  |
+--------+------------+---------------+----------+

---

🎯 Future Enhancements

* 📊 Add category-wise expense charts
* 💡 Introduce budget alerts and savings goals
* 🪟 GUI version using Tkinter / PyQt
* 📈 Generate monthly reports in Excel or PDF
* ☁️ Cloud sync or database integration

---

💬 About the Project

This project demonstrates:
* Practical usage of Python fundamentals
* Real-world file I/O operations
* Designing modular and reusable code
* A foundation for finance management apps
