from pathlib import Path
from datetime import datetime, timedelta,date,time
from utils.file_handler import load_file, save_file
from utils.displays import print_order_details
from utils.validations import validate_input
from room.rooms_manaegment import validate_room_id,load_rooms,validate_if_room_is_active,get_room_id_input,find_room_by_id
from utils.time_manaegment import *
order_file_path = Path("order/orders.json")



def load_orders():
    if not order_file_path.exists():
        print("No orders available.")
        return 
    return load_file(order_file_path)

def add_order_to_file(order):
    orders = load_orders()
    orders.append(order)
    save_file(order_file_path, orders)


def create_new_order():
    return {
        "booking_id": f"B{len(load_orders()) + 1:03d}",
        "customer_name": "",
        "room_id": "",
        "booking_date": "",
        "start_time": "",
        "players": 0,
        "total_price": 0.0,
        "status": "Active",
        "cancellation_fee": 0.0}

def display_orders():
    orders = load_orders()
    for order in orders:
        print_order_details(order)

def discount_order(order):
    if 1 <= order["players"] <= 4:
        return 0
    elif 5 <= order["players"] <= 6:
        return 0.10
    elif order["players"] >= 7:
        return 0.15
    else:
        return 0
    

def calculate_total_price(order, room):
    base_price = order["players"] * room["price_per_player"]
    discount = discount_order(order)
    price_after_discount = base_price * (1 - discount)
    if is_weekend(order["booking_date"]):
        price_after_discount = price_after_discount * 1.15
    return round(price_after_discount, 2)

def is_weekend(date_str):
    booking_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    return booking_date.weekday() in [4, 5]


def create_order():
    rooms = load_rooms()
    orders = load_orders()
    new_order = create_new_order()
    room_id = get_room_id_input("Enter Room ID: ")
    if not validate_room_id(room_id):
        return
    if not validate_if_room_is_active(room_id):
        return
    room = find_room_by_id(rooms, room_id)
    new_order["room_id"] = room_id
    new_order["customer_name"] = validate_input("Enter customer name: ", "non_empty")
    new_order["players"] = get_players_input(room)
    date_str, time_str = geting_date_an_time_input()
    if not validating_room_avalability(orders, room, date_str, time_str):
        print(f"Room {room['name']} is not available at the selected time.")
        return
    new_order["booking_date"] = date_str
    new_order["start_time"] = time_str
    new_order["total_price"] = calculate_total_price(new_order, room)
    add_order_to_file(new_order)
    print(f"Order {new_order['booking_id']} created successfully. Total price: ${new_order['total_price']:.2f}")


def validating_room_avalability(orders, room, date_str, time_str):
    booking_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    end_time = booking_datetime + timedelta(minutes=room['duration'] + 15)
    for order in orders:
        if order['room_id'] == room['room_id'] and order['status'] == 'Active':
            existing_booking_datetime = datetime.strptime(f"{order['booking_date']} {order['start_time']}", "%Y-%m-%d %H:%M")
            existing_end_time = existing_booking_datetime + timedelta(minutes=room['duration'] + 15)
            if (booking_datetime < existing_end_time and end_time > existing_booking_datetime):
                return False
    return True




def validate_players_in_room_range(players, room):
    if room['min_players'] <= players <= room['max_players']:
        return True
    print(f"Number of players must be between {room['min_players']} and {room['max_players']}.")
    return False

def get_players_input(room):
    while True:
        players = validate_input(f"Enter number of players ({room['min_players']}-{room['max_players']}): ", "positive_int")
        if validate_players_in_room_range(players, room):
            return players

def get_order_id_input(message):
    room_id = validate_input(message, "positive_int")
    return f"B{int(room_id):03d}"

def search_order_by_id():
    orders = load_orders()
    order_id = get_order_id_input("Enter the Booking ID to search: ")
    for order in orders:
        if order["booking_id"] == order_id:
            print_order_details(order)
            return
    print(f"No order found with ID: {order_id}")

def search_order_by_customer_name():
    orders = load_orders()
    customer_name = validate_input("Enter the customer name to search: ", "non_empty")
    found_orders = [order for order in orders if order["customer_name"].lower() == customer_name.lower()]
    if found_orders:
        for order in found_orders:
            print_order_details(order)
    else:
        print(f"No orders found for customer: {customer_name}")


def search_order_by_date():
    orders = load_orders()
    date_str = validate_input("Enter the booking date to search (YYYY-MM-DD): ", "non_empty")
    if not validate_date_input(date_str):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    found_orders = [order for order in orders if order["booking_date"] == date_str]
    if found_orders:
        for order in found_orders:
            print_order_details(order)
    else:
        print(f"No orders found for date: {date_str}")


def update_order():# can update data or start time or number of players: valitaions!!!
    orders = load_orders()
    order_id = get_order_id_input("Enter the Booking ID to update: ")
    for order in orders:
        if order["booking_id"] == order_id:
            print("Current order details:")
            print_order_details(order)
            print("Enter new details (leave blank to keep current value):")
            new_customer_name = input(f"Customer Name [{order['customer_name']}]: ").strip()
            if new_customer_name:
                order["customer_name"] = new_customer_name
            rooms = load_rooms()
            room = find_room_by_id(rooms, order["room_id"])
            new_players = input(f"Number of Players [{order['players']}]: ").strip()
            if new_players:
                new_players = int(new_players)
                if validate_players_in_room_range(new_players, room):
                    order["players"] = new_players
                else:
                    print(f"Invalid number of players. Keeping previous value: {order['players']}")
            date_str, time_str = geting_date_an_time_input()
            if validating_room_avalability(orders, room, date_str, time_str):
                order["booking_date"] = date_str
                order["start_time"] = time_str
            else:
                print(f"Room {room['name']} is not available at the selected time. Keeping previous date and time.")
            order["total_price"] = calculate_total_price(order, room)
            save_file(order_file_path, orders)
            print(f"Order {order_id} updated successfully.")
            return
    print(f"No order found with ID: {order_id}")

def cenceling_order(): # calling order and changing status to cencelled and adding cencel fee
    orders = load_orders()
    order_id = get_order_id_input("Enter the Booking ID to cancel: ")
    for order in orders:
        if order["booking_id"] == order_id:
            print("Current order details:")
            print_order_details(order)
            date_str = order["booking_date"]
            time_str = order["start_time"]
            cancellation_fee_percentage = cencel_order_fee(date_str, time_str)
            if cancellation_fee_percentage > 0:
                room = find_room_by_id(load_rooms(), order["room_id"])
                cancellation_fee = calculate_total_price(order, room) * cancellation_fee_percentage
                order["cancellation_fee"] = round(cancellation_fee, 2)
                print(f"Cancellation fee: ${order['cancellation_fee']:.2f}")
            else:
                order["cancellation_fee"] = 0.0
                print("No cancellation fee.")
            order["status"] = "Cancelled"
            save_file(order_file_path, orders)
            print(f"Order {order_id} cancelled successfully.")
            return
    print(f"No order found with ID: {order_id}")

def cencel_order_fee(date_str, time_str):#TODO more then 1 day free, btween 6-24 hours 25% ' less then 6 hours 50% fee
    booking_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    current_datetime = datetime.now()
    time_difference = booking_datetime - current_datetime
    if time_difference > timedelta(days=1):
        return 0.0  
    elif timedelta(hours=6) < time_difference <= timedelta(days=1):
        return 0.25  
    elif time_difference <= timedelta(hours=6):
        return 0.50  
    else:
        return 0.0  