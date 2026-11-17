from utils.displays import print_reports_menu
from reports.reports_management import *


def reports_main():
    while True:
        print_reports_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            display_active_orders()
            pass
        elif choice == "2":
            display_canceled_orders()
            pass
        elif choice == "3":
            display_revenue_from_active_orders()
            pass
        elif choice == "4":
            display_revenue_from_canceled_orders()
            pass
        elif choice == "5":
            display_most_popular_room()
            pass
        elif choice == "6":
            display_number_of_orders_per_room()
            pass
        elif choice == "7":
            display_occupancy_rate_of_rooms()# TODO 
            pass
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")




