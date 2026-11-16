from utils.displays import print_orders_menu
from order.orders_management import *

def order_main():
    while True:
        print_orders_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            create_order()
        elif choice == "2":
            display_orders()
            pass
        elif choice == "3":
            search_order_by_id()
        elif choice == "4":
            search_order_by_customer_name()
            pass
        elif choice == "5":
            search_order_by_date()
            pass
        elif choice == "6":
            update_order()
            pass
        elif choice == "7":
            cenceling_order()
            pass
        elif choice == "8":
            break 
        else:
            print("Invalid choice. Please try again.")