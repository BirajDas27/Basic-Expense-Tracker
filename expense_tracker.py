import os
import sys
from tabulate import tabulate

class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        if not os.path.exists('expenses.csv'):
            print('No file was found, creating a new file.')
            with open('expenses.csv', 'w') as file:
                file.write(f'1,{expense.date},{expense.description},{expense.amount}\n')
                return

        with open('expenses.csv', 'r') as file:
            line = file.readlines()
            last_index = len(line)
        with open('expenses.csv', 'a') as file:
            file.write(f'{last_index+1},{expense.date},{expense.description},{expense.amount}\n')

    def view_expense(self):
        if not os.path.exists('expenses.csv'):
            print('No file named expenses found in common directory.')
            return

        with open('expenses.csv', 'r') as file:
            lines = file.readlines()

            if len(lines) == 0:
                print('\nNo expense found, list is empty.')
                return

            data = []
            for line in lines:
                row = line.strip().split(',')
                data.append(row)

        headers = ['Index', 'Date', 'Description', 'Amount']
        print('\nExpense List:\n-------------')
        print(tabulate(data, headers=headers, tablefmt='grid'))

    def update_expense(self):
        if not os.path.exists('expenses.csv'):
            print('No file named expenses found in common directory.')
            return

        with open('expenses.csv', 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print('\nNo expense found, list is empty.')
                return

            else:
                i = int(input('\nEnter the index you want to edit: '))
                date = input('Enter date in dd-mm-yyyy format: ')
                description = input('Enter category of expense: ')
                amount = float(input('Enter expense amount: '))

                lines[i-1] = f'{i},{date},{description},{amount}\n'
                with open('expenses.csv', 'w') as file:
                    file.writelines(lines)



    def remove_expense(self):
        if not os.path.exists('expenses.csv'):
            print('No file named expenses found in common directory.')
            return

        updated_list = []
        with open('expenses.csv', 'r') as file:
            lines = file.readlines()

        if len(lines) == 0:
            print('\nNo expense found, list is empty.')
            return

        try:
            i = int(input('\nEnter the index you want to remove: '))
        except ValueError:
            print('Invalid input. Please enter a number.')
            return

        if 0 < i <= len(lines):
            del lines[i - 1]
            for i, line in enumerate(lines, start = 1):
                if len(line.split(',')) == 4:
                    index, date, description, amount = line.split(',')
                else:
                    date, description, amount = line.split(',')

                if i == 1:
                    with open('expenses.csv', 'w') as file:
                        new_lines = (f'{i},{date},{description},{amount}')
                        file.writelines(new_lines)
                else:
                    with open('expenses.csv', 'a') as file:
                        new_lines = (f'{i},{date},{description},{amount}')
                        file.write(new_lines)

            print('\nExpense removed successfully.')
        else:
            print('\nIndex out of range.')


    def total_expenses(self):
        if not os.path.exists('expenses.csv'):
            print('No file named expenses found in common directory.')
            return

        with open('expenses.csv', 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print('\nNo expense found, list is empty.')
            else:
                data = []
                total = 0
                for line in lines:
                    row = line.strip().split(',')
                    data.append(row)
                    parts = line.split(',')
                    amount = float(parts[3])
                    total += amount

                headers = ['Index', 'Date', 'Description', 'Amount']
                #print('\nExpense List:\n-------------')
                #print(tabulate(data, headers=headers, tablefmt='grid'))
                print(f'\nTotal Expenses: ₹{total:.2f}')

    def search_expense(self):
        if not os.path.exists('expenses.csv'):
            print('No file named expenses found in common directory.')
            return

        data = []
        total = 0
        with open('expenses.csv', 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print('\nNo expense found, list is empty.')
                return
            else:
                search_key = input('\nEnter description to search: ').strip().lower()
                for line in lines:
                    parts = line.strip().split(',')
                    idx, date, desc, amount = parts
                    if search_key in desc.lower():
                        data.append([idx, date, desc, amount])
                        amt = float(amount)
                        total += amt

                if data:
                    print(f"\nExpenses matching '{search_key}':")
                    headers = ['Index', 'Date', 'Description', 'Amount']
                    print(tabulate(data, headers=headers, tablefmt='grid'))
                    print(f'Total expenditure for {search_key}: {total}')
                else:
                    print(f"\nNo expenses found matching '{search_key}'.")

    def sort(self):
        if not os.path.exists('expenses.csv'):
            print('No file named expenses found in common directory.')
            return

        with open('expenses.csv', 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print('\nNo expense found, list is empty.')
                return
            else:
                sorted = []
                for line in lines:
                    parts = line.strip().split(',')
                    idx, date, description, amount = parts
                    sorted.append([int(idx), date, description, float(amount)])
                    
                opt = input('\nSort the amount(asce/desc): ').lower().strip()
                reverse = True if opt == 'desc' else False
                sorted.sort(key = lambda x: x[3], reverse = reverse)

                for i, row in enumerate(sorted, start = 1):
                    row[0] = i

                headers = ['Index', 'date', 'description', 'Amount']
                print(tabulate(sorted, headers = headers, tablefmt = 'grid'))

    def selective_total(self):
        if not os.path.exists('expenses.csv'):
            print('No file named expenses found in common directory.')
            return

        with open('expenses.csv', 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print('\nNo expense found, list is empty.')
                return

            data = []
            total = 0
            headers = ['Index', 'Date', 'Description', 'Amount']
            
            inp_year = input('Enter year(xxxx): ')
            inp_month = input('Enter month(xx): ')

            
            for line in lines:
                parts = line.split(',')
                idx, date, description, amount = parts
                year, month, day = date.strip().split('-')

                if (inp_year+'-'+inp_month) == (year+'-'+month):
                    data.append([idx, date, description, float(amount)])

            for i, row in enumerate(data, start = 1):
                row[0] = i
                total += row[3]
            
            if not data:
                print('\nNo expense info found for provided input.')
                return
                
            else:
                print(tabulate(data, headers = headers, tablefmt='grid'))
                print(f'Total expenditure: {total}')

def main():
    tracker = ExpenseTracker()
    while True:
        print('\nExpense Tracker Menu\n----------------------')
        print('1. Add expense.')
        print('2. View expenses.')
        print('3. Update expense')
        print('4. Remove expense.')
        print('5. Total expenditure.')
        print('6. Search expense.')
        print('7. Sort expenses (amount).')
        print('8. Yearly/monthly expense.')
        print('9. Exit.')
        opt = int(input('Enter your requirement: '))

        if opt == 1:
            date = input('Enter date in yyyy-mm-dd format: ')
            description = input('Enter category of expense: ')
            amount = float(input('Enter expense amount: '))

            expense = Expense(date, description, amount)
            tracker.add_expense(expense)
            print('New expense added successfully.')

        elif opt == 2:
            tracker.view_expense()

        elif opt == 3:
            tracker.update_expense()

        elif opt == 4:
            tracker.remove_expense()

        elif opt == 5:
            tracker.total_expenses()

        elif opt == 6:
            tracker.search_expense()

        elif opt == 7:
            tracker.sort()

        elif opt == 8:
            tracker.selective_total()

        elif opt == 9:
            sys.exit()

        else:
            print('Invalid unput!!')


main()