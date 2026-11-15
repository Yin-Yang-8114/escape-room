from displays import print_main_menu
from rooms import room_main
from orders import order_main
from reports import reports_main


def main():
    while True:
        print_main_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            room_main() 
            pass
        elif choice == "2":
            order_main()
            pass
        elif choice == "3":
            reports_main()
            pass
        elif choice == "4":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()