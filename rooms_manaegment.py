from pathlib import Path
from file_handler import load_file, save_file
from validations import validate_input
from displays import print_room_details,print_update_room_menu
rooms_file_path = Path("rooms.json")

def add_room_to_file(room):
    rooms = load_rooms()
    rooms.append(room)
    save_file(rooms_file_path, rooms)


def create_new_room():
    return {
        "room_id": f"R{len(load_rooms()) + 1:03d}",
        "name": "",
        "difficulty": "",
        "duration": 0,
        "min_players": 0,
        "max_players": 0,
        "price_per_player": 0.0,
        "is_active": True}

def load_rooms():
    if not rooms_file_path.exists():
        print("No rooms available.")
        return
    return load_file(rooms_file_path)


def display_rooms():
    rooms = load_rooms()
    for room in rooms:
        print_room_details(room)

def display_room_details():
    rooms = load_rooms()
    room_id = validate_input("Enter the Room ID to view details: ","positive_int")
    room_id = f"R{int(room_id):03d}"
    for room in rooms:
        if room['room_id'] == room_id:
            print_room_details(room)
            return
    else:
        print(f"No room found with ID: {room_id}")


def add_room():
    new_room = create_new_room()
    new_room['name'] = validate_input("Enter room name: ", "non_empty")
    new_room['difficulty'] = validate_input("Enter room difficulty (easy, medium, hard): ", "non_empty").lower()
    # if new_room['difficulty'] not in ['easy', 'medium', 'hard']:
    #     print("Invalid difficulty level. Please enter 'easy', 'medium', or 'hard'.")
    #     return
    if not validate_room_difficulty(new_room["difficulty"]):
        return
    new_room['duration'] = validate_input("Enter room duration in minutes: ", "positive_int")
    new_room['min_players'] = validate_input("Enter minimum number of players: ", "positive_int")
    new_room['max_players'] = validate_input("Enter maximum number of players: ", "positive_int")
    # if new_room['min_players'] > new_room['max_players']:
    #     print("Minimum players cannot be greater than maximum players.")
    #     return
    if not validate_room_min_max_players(new_room["min_players"],new_room["max_players"]):
        return
    new_room['price_per_player'] = validate_input("Enter price per player: ", "positive_int")
    add_room_to_file(new_room)
    print(f"Room {new_room['room_id']} added successfully.")


def validate_room_difficulty(difficulty):
    if difficulty.lower() not in ['easy', 'medium', 'hard']:
        print("Invalid difficulty level. Please enter 'easy', 'medium', or 'hard'.")
        return False
    return True

def validate_room_min_max_players(min_players, max_players):
    if min_players > max_players:
        print("Minimum players cannot be greater than maximum players.")
        return False
    return True

def update_room():
    pass
    rooms = load_rooms()
    room_id = validate_input("Enter the Room ID to update: ", "positive_int")
    room_id = f"R{int(room_id):03d}"
    for room in rooms:
        if room['room_id'] == room_id:
            while True:
                print_update_room_menu()
                choice = input("Enter your choice: ")
                if choice == "1":
                    room['name'] = validate_input("Enter new room name: ", "non_empty")
                elif choice == "2":
                    new_difficulty = validate_input("Enter new room difficulty (easy, medium, hard): ", "non_empty").lower()
                    if not validate_room_difficulty(new_difficulty):
                        continue
                    room['difficulty'] = new_difficulty
                elif choice == "3":
                    room['duration'] = validate_input("Enter new room duration in minutes: ", "positive_int")
                elif choice == "4":
                    new_min_players = validate_input("Enter new minimum number of players: ", "positive_int")
                    if not validate_room_min_max_players(new_min_players, room['max_players']):
                        continue
                    room['min_players'] = new_min_players
                elif choice == "5":
                    new_max_players = validate_input("Enter new maximum number of players: ", "positive_int")
                    if not validate_room_min_max_players(room['min_players'], new_max_players):
                        continue
                    room['max_players'] = new_max_players
                elif choice == "6":
                    room['price_per_player'] = validate_input("Enter new price per player: ", "positive_int")
                elif choice == "7":
                    break 
                else:
                    print("Invalid choice. Please try again.")
            save_file(rooms_file_path, rooms)
            print(f"Room {room_id} updated successfully.")
            return
    else:
        print(f"No room found with ID: {room_id}")

def disable_room():
    rooms = load_rooms()
    room_id = validate_input("Enter the Room ID to disable: ", "positive_int")
    room_id = f"R{int(room_id):03d}"
    for room in rooms:
        if room['room_id'] == room_id:
            if not room['is_active']:
                print(f"Room {room_id} is already disabled.")
                return
            room['is_active'] = False
            save_file(rooms_file_path, rooms)
            print(f"Room {room_id} has been disabled.")
            return
    else:
        print(f"No room found with ID: {room_id}")
