from utils.displays import print_rooms_menu
from room.rooms_manaegment import *

def room_main():
    while True:
        print_rooms_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            display_rooms()
        elif choice == "2":
            display_room_details()
        elif choice == "3":
            add_room()
        elif choice == "4":
            update_room()
            pass
        elif choice == "5":
            disable_room()
        elif choice == "6":
            break 
        else:
            print("Invalid choice. Please try again.")
