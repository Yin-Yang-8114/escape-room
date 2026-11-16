from utils.displays import print_orders_menu
from order.orders_management import *

def order_main():
    while True:
        print_orders_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            create_order()
        elif choice == "2":
            # Call the function to display orders
            pass
        elif choice == "3":
            # Call the function to search order by Id
            pass
        elif choice == "4":
            # Call the function to search order by customer name
            pass
        elif choice == "5":
            # Call the function to search order by date
            pass
        elif choice == "6":
            # Call the function to update an order
            pass
        elif choice == "7":
            # Call the function to cancel an order
            pass
        elif choice == "8":
            break  # Go back to the main menu
        else:
            print("Invalid choice. Please try again.")