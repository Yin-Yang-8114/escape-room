from utils.file_handler import load_file
from room.rooms_manaegment import load_rooms
from utils.displays import print_order_details
from order.orders_management import load_orders

def display_active_orders():
    orders = load_orders()
    active_orders = [order for order in orders if order["status"] == "Active"]
    for order in active_orders:
        print_order_details(order)

def display_canceled_orders():
    orders = load_orders()
    canceled_orders = [order for order in orders if order["status"] == "Canceled"]
    for order in canceled_orders:
        print_order_details(order)

def display_revenue_from_active_orders():
    orders = load_orders()
    active_orders = [order for order in orders if order["status"] == "Active"]
    total_revenue = sum(order["total_price"] for order in active_orders)
    print(f"Total revenue from active orders: ${total_revenue:.2f}")


def display_revenue_from_canceled_orders():
    orders = load_orders()
    canceled_orders = [order for order in orders if order["status"] == "Canceled"]
    total_revenue = sum(order["total_price"] for order in canceled_orders)
    print(f"Total revenue from canceled orders: ${total_revenue:.2f}")

def display_most_popular_room():
    orders = load_orders()
    rooms = load_rooms()
    room_order_count = {room["room_id"]: 0 for room in rooms}
    for order in orders:
        if order["status"] == "Active":
            room_order_count[order["room_id"]] += 1
    most_popular_room_id = max(room_order_count,key=room_order_count.get)
    most_popular_room = next(room for room in rooms if room["room_id"] == most_popular_room_id)
    print(f"The most popular room is: {most_popular_room['name']} with {room_order_count[most_popular_room_id]} active orders.")

def display_number_of_orders_per_room():
    orders = load_orders()
    rooms = load_rooms()
    room_order_count = {room["room_id"]: 0 for room in rooms}
    for order in orders:
        if order["status"] == "Active":
            room_order_count[order["room_id"]] += 1
    for room in rooms:
        print(f"Room: {room['name']} - Number of active orders: {room_order_count[room['room_id']]}")

def display_occupancy_rate_of_rooms():
    pass


def calculate_occupancy_rate():
    pass

