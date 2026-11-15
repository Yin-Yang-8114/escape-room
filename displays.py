def print_main_menu():
    print("Welcome to the Escape Room Game!")
    print("1. rooms menegmant")
    print("2. orders management")
    print("3. reports management")
    print("4. exit")

def print_rooms_menu():
    print("Rooms Management Menu:")
    print("1. display rooms")
    print("2. ddisplay room details")
    print("3. add room")
    print("4. update room")
    print("5. delete room")
    print("6. back to main menu")


def print_orders_menu():
    print("Orders Management Menu:")
    print("1. create order")
    print("2. display orders")
    print("3. search order by Id")
    print("4. search order by customer name")
    print("5. search order by date")
    print("6. update order")
    print("7. cancel order")
    print("8. back to main menu")

def print_reports_menu():
    print("Reports Management Menu:")
    print("1. display all active orders")
    print("2. display all cenceled orders")
    print("3. display all revenue from active orders")
    print("4. display all revenue from canceled payment orders")
    print("5. display the most popular room")
    print("6. display number of orders per room")
    print("7. display occupancy rate of rooms")
    print("8. back to main menu")


def print_room_details(room):
    print(f"Room ID: {room['room_id']}, Name: {room['name']}, Difficulty: {room['difficulty']}, Duration: {room['duration']} minutes, Players: {room['min_players']}-{room['max_players']}, Price per Player: ${room['price_per_player']:.2f}, Active: {'Yes' if room['is_active'] else 'No'}")


def print_update_room_menu():
    print("Update Room Menu:")
    print("1. Update room name")
    print("2. Update room difficulty")
    print("3. Update room duration")
    print("4. Update minimum players")
    print("5. Update maximum players")
    print("6. Update price per player")
    print("7. Back to rooms menu")

def print_order_details(order):
    print(f"Booking ID: {order['booking_id']}, Customer Name: {order['customer_name']}, Room ID: {order['room_id']}, Booking Date: {order['booking_date']}, Start Time: {order['start_time']}, Players: {order['players']}, Total Price: ${order['total_price']:.2f}, Status: {order['status']}, Cancellation Fee: ${order['cancellation_fee']:.2f}")