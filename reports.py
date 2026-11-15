from displays import print_reports_menu



def reports_main():
    while True:
        print_reports_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            # Call the function to display all active orders
            pass
        elif choice == "2":
            # Call the function to display all canceled orders
            pass
        elif choice == "3":
            # Call the function to display all revenue from active orders
            pass
        elif choice == "4":
            # Call the function to display all revenue from canceled payment orders
            pass
        elif choice == "5":
            # Call the function to display the most popular room
            pass
        elif choice == "6":
            # Call the function to display number of orders per room
            pass
        elif choice == "7":
            # Call the function to display occupancy rate of rooms
            pass
        elif choice == "8":
            break  # Go back to the main menu
        else:
            print("Invalid choice. Please try again.")




