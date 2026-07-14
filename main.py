from expence_tracker import *

while True:
     print("\n========== Expence Tracker ==========")

     print("1 : Add Expence")
     print("2 : View Expences")
     print("3 : update Expences")
     print("4 : Delete Expences")
     print("5 : Exit")

     choice = int(input("Enter your choice : "))

     if choice == 1:
          add_expence()
    
     elif choice == 2:
          view_expences()

     elif choice == 3:
          update()

     elif choice == 4:
          delete()

     elif choice == 5:
          print("Thank You")
          break