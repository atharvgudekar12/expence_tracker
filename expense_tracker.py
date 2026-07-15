from db import expenses
from datetime import datetime


def add_expense():
    amount = int(input("Enter the amount: "))
    description = input("Enter the description: ")

    date = datetime.now().strftime("%d-%m-%Y")

    expense = {
        "Amount": amount,
        "Description": description,
        "Date": date
    }

    expenses.insert_one(expense)

    print("Expense added successfully.")


def view_expenses():
    data = list(expenses.find())

    if len(data) == 0:
        print("No expenses found.")
        return

    for expense in data:
        print(
            f"ID: {expense['_id']} | "
            f"Date: {expense.get('Date', 'No Date')} | "
            f"Amount: {expense['Amount']} | "
            f"Description: {expense['Description']}"
        )


def update():

    date = input("Enter the date to update the expense (DD-MM-YYYY): ")

    expense_list = list(expenses.find({"Date": date}))

    if len(expense_list) == 0:
        print("No expenses found for this date.")
        return

    print("\nExpenses:\n")

    for i, expense in enumerate(expense_list, start=1):
        print(
            f"{i}. Amount: {expense['Amount']} | "
            f"Description: {expense['Description']} | "
            f"Date: {expense['Date']}"
        )

    choice = int(input("\nEnter the expense number to update: "))

    if choice < 1 or choice > len(expense_list):
        print("Invalid choice.")
        return

    selected = expense_list[choice - 1]

    amount = int(input("Enter the new amount: "))
    description = input("Enter the new description: ")

    expenses.update_one(
        {"_id": selected["_id"]},
        {
            "$set": {
                "Amount": amount,
                "Description": description
            }
        }
    )

    print("Expense updated successfully.")

def delete_expense():

    date = input("Enter the date (DD-MM-YYYY): ")

    expense_list = list(expenses.find({"Date": date}))

    if len(expense_list) == 0:
        print("No expenses found for this date.")
        return

    print("\nExpenses:\n")

    for i, expense in enumerate(expense_list, start=1):
        print(
            f"{i}. Amount: {expense['Amount']} | "
            f"Description: {expense['Description']} | "
            f"Date: {expense['Date']}"
        )

    choice = int(input("\nEnter the expense number to delete: "))

    if choice < 1 or choice > len(expense_list):
        print("Invalid choice.")
        return

    selected = expense_list[choice - 1]

    expenses.delete_one({"_id": selected["_id"]})

    print("Expense deleted successfully.")