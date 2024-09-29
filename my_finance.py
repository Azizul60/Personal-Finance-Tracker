#Add Income: 
#Add Expenses:  (e.g., food, transport, bills), amounts, and dates.
#View Current Balance:  (income minus expenses).
#Monthly Report: Generate a report showing total income and expenses for the current or selected month.
#Expense Breakdown by Category: 
#Saving and Loading Data

import json
import os
from datetime import datetime

def main():
    ...
    
    filename = 'finance_data.json'
    data = load_finance(filename)

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Current Balance")
        print("4. View Monthly Report")
        print("5. View Expense Breakdown by Category")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            view_balance(data)
        elif choice == '4':
            monthly_report(data)
        elif choice == '5':
            expense_breakdown(data)
        elif choice == '6':
            save_tasks(filename, data)
            break
        else:
            print("Invalid choice, please try again.")




def load_finance(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {"income":[] ,"expenses":[]}

def save_tasks(filename, data):
    # Save tasks to the file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def add_income(data):
    amount = float(input("Enter income amount: "))
    description = input("Enter description of income: ")
    date = input("Enter date (YYYY-MM-DD): ")
    
    data['income'].append({
        "amount": amount,
        "description": description,
        "date": date
    })


def add_expense(data):
    amount = float(input("Enter expense amount: "))
    description = input("Enter description of expense: ")
    category = input("Enter category (e.g., Food, Transport, Bills): ")
    date = input("Enter date (YYYY-MM-DD): ")

    data['expenses'].append({
        "amount": amount,
        "description": description,
        "category": category,
        "date": date
    })


def view_balance(data):
    total_income = sum(item['amount'] for item in data['income'])
    total_expenses = sum(item['amount'] for item in data['expenses'])
    balance = total_income - total_expenses
    print(f"Current Balance: ${balance:.2f}")

def monthly_report(data):
    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")

    total_income = 0
    total_expenses = 0

    for income in data['income']:
        if income['date'].startswith(f"{year}-{month}"):
            total_income += income['amount']

    for expense in data['expenses']:
        if expense['date'].startswith(f"{year}-{month}"):
            total_expenses += expense['amount']

    print(f"Income for {month}/{year}: ${total_income:.2f}")
    print(f"Expenses for {month}/{year}: ${total_expenses:.2f}")
    print(f"Net for {month}/{year}: ${total_income - total_expenses:.2f}")


def expense_breakdown(data):
    categories = {}
    for expense in data['expenses']:
        category = expense['category']
        categories[category] = categories.get(category, 0) + expense['amount']

    print("\nExpense Breakdown by Category:")
    for category, total in categories.items():
        print(f"{category}: ${total:.2f}")





if __name__=="__main__":
    main()