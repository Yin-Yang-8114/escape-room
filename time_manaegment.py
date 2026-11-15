from datetime import date,time,datetime

# date_str = input("Enter booking date (YYYY-MM-DD): ")

# def validate_date(date_str):
#     try:
#         dateObject = datetime.strptime(date_str,'%d/%m%Y')
#         return True
#     except ValueError:
#         return False
# print(validate_date(date_str))

def validate_date_input(date_str):
        try:
            dateObject = datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False



def validate_time_input(time_str):
    try:
        timeObject = datetime.strptime(time_str, '%H:%M')
        return True
    except ValueError:
        return False

def geting_date_an_time_input():
    while True:
        date_str = input("Enter booking date (YYYY-MM-DD): ")
        if validate_date_input(date_str):
            break
        else:
            print("Invalid date format. Please enter a valid date in YYYY-MM-DD format.")
    while True:
        time_str = input("Enter start time (HH:MM): ")
        if validate_time_input(time_str):
            break
        else:
            print("Invalid time format. Please enter a valid time in HH:MM format.")
    return date_str, time_str

