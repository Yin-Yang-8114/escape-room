from pathlib import Path
from datetime import datetime, timedelta,date,time
from file_handler import load_file, save_file
from displays import print_order_details
from validations import validate_input
from rooms_manaegment import validate_room_id,load_rooms,validate_if_room_is_active
from time_manaegment import geting_date_an_time_input
order_file_path = Path("orders.json")



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
        "booking_id": f"R{len(load_orders()) + 1:03d}",
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
    elif 7 <= order["players"] <= 8:
        return 0.15
    else:
        return 0
    


def validate_room_availability():
    pass

def create_order():
    pass



