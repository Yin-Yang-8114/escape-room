from pathlib import Path
from utils.file_handler import load_file, save_file
from utils.validations import validate_input
from utils.displays import print_room_details,print_update_room_menu
rooms_file_path = Path("room/rooms.json")

def load_rooms():
    if not rooms_file_path.exists():
        print("No rooms available.")
        return []
    return load_file(rooms_file_path)

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

def get_room_id_input(message):
    room_id = validate_input(message, "positive_int")
    return f"R{int(room_id):03d}"

def find_room_by_id(rooms, room_id):
    for room in rooms:
        if room['room_id'] == room_id:
            return room
    return None

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

def get_room_difficulty():
    while True:
        difficulty = validate_input("Enter room difficulty (easy, medium, hard): ", "non_empty")
        if validate_room_difficulty(difficulty):
            return difficulty.capitalize()
        
def get_min_players(max_players=None):
    while True:
        min_players = validate_input("Enter minimum number of players: ", "positive_int")
        if max_players is None or validate_room_min_max_players(min_players, max_players):
            return min_players

def get_max_players(min_players):
    while True:
        max_players = validate_input("Enter maximum number of players: ", "positive_int")
        if validate_room_min_max_players(min_players, max_players):
            return max_players



def display_rooms():
    rooms = load_rooms()
    for room in rooms:
        print_room_details(room)

def display_room_details():
    rooms = load_rooms()
    room_id = get_room_id_input("Enter the Room ID to view details: ")
    room = find_room_by_id(rooms, room_id)
    if room:
        print_room_details(room)
    else:
        print(f"No room found with ID: {room_id}")

def add_room():
    new_room = create_new_room()
    new_room['name'] = validate_input("Enter room name: ", "non_empty")
    new_room['difficulty'] = get_room_difficulty()
    new_room['duration'] = validate_input("Enter room duration in minutes: ", "positive_int")
    new_room['min_players'] = get_min_players()
    new_room['max_players'] = get_max_players(new_room['min_players'])
    new_room['price_per_player'] = validate_input("Enter price per player: ", "positive_int")
    add_room_to_file(new_room)
    print(f"Room {new_room['room_id']} added successfully.")

def update_room():
    rooms = load_rooms()
    room_id = get_room_id_input("Enter the Room ID to update: ")
    room = find_room_by_id(rooms, room_id)
    if not room:
        print(f"No room found with ID: {room_id}")
        return
    while True:
        print_update_room_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            room['name'] = validate_input("Enter new room name: ", "non_empty")
        elif choice == "2":
            room['difficulty'] = get_room_difficulty()
        elif choice == "3":
            room['duration'] = validate_input("Enter new room duration in minutes: ", "positive_int")
        elif choice == "4":
            room['min_players'] = get_min_players(room['max_players'])
        elif choice == "5":
            room['max_players'] = get_max_players(room['min_players'])
        elif choice == "6":
            room['price_per_player'] = validate_input("Enter new price per player: ", "positive_int")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")
    save_file(rooms_file_path, rooms)
    print(f"Room {room_id} updated successfully.")

def disable_room():
    rooms = load_rooms()
    room_id = get_room_id_input("Enter the Room ID to enable/disable: ")
    room = find_room_by_id(rooms, room_id)
    if not room:
        print(f"No room found with ID: {room_id}")
        return
    room['is_active'] = not room['is_active']
    save_file(rooms_file_path, rooms)
    status = "enabled" if room['is_active'] else "disabled"
    print(f"Room {room_id} has been {status}.")

def validate_room_id(room_id):
    rooms = load_rooms()
    if find_room_by_id(rooms, room_id):
        return True
    print(f"No room found with ID: {room_id}")
    return False

def validate_if_room_is_active(room_id):
    rooms = load_rooms()
    room = find_room_by_id(rooms, room_id)
    if room and room['is_active']:
        return True
    print(f"Room {room_id} is not active.")
    return False