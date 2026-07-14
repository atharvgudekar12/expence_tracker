from expense_tracker import *

while True:

    print("\n========== Expense Tracker ==========")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_expenses()

    elif choice == 3:
        update()

    elif choice == 4:
        delete_expense()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")