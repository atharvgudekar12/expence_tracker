from db import expence_tracker
from datetime import datetime;


def add_expence() :
    amount = int(input("Enter the amount : "))
    description = input("Enter the description : ")
    date = datetime.now().strftime("%d-%m-%Y")

    expence = {
        "Amount" : amount,
        "Description" : description,
        "Date" : date,
    }
      
    result = expence_tracker.insert_one(expence)

    print("Expence is added successfully")

def view_expences():
    data = expence_tracker.find()

    for expence in data:
        print(
        f"ID: {expence['_id']} | "
        f"Date: {expence.get('Date', 'No Date')} |"
        f"Amount: {expence['Amount']} | "
        f"Description: {expence['Description']}"
    )

        if len(expence) == 0:
            print("No expences are found")
            break


def update():
    find = input("uodate by entering date :")
    update = expence_tracker.update_one(find, expence_tracker.find())


def delete():
    
    date = input("Enter the date to delete : ")

    expences = list(expence_tracker.find({"Date": date}))

    if len(expences) == 0:
        print("No expences found for the given date.")
        return
    
    print("\nExpences:")

    for i, expence in enumerate(expences, start=1):
         print(f"{i}. Amount: {expence['Amount']}  Description: {expence['Description']}  Date: {expence['Date']}")
    
    choice = int(input("Enter the number of expences to delete : "))

    selected = expences[choice - 1]  #beacuse list use the index from 0 to count

    expence_tracker.delete_one({"_id": selected["_id"]})
    print("Expense deleted successfully.")