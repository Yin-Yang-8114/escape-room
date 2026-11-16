from datetime import date,time,datetime

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

def validate_time_range(time_str):
    try:
        timeObject = datetime.strptime(time_str, '%H:%M').time()
        if time(10, 0) <= timeObject <= time(22, 0):
            return True
        else:
            return False
    except ValueError:
        return False

def validate_date_range(date_str, time_str):# TODO split to two func
    try:
        dateObject = datetime.strptime(date_str, '%Y-%m-%d').date()
        timeObject = datetime.strptime(time_str, '%H:%M').time()
        currentDate = date.today()
        currentTime = datetime.now().time()
        if dateObject < currentDate:
            return False
        elif dateObject == currentDate and timeObject < currentTime:
            return False
        else:
            return True
    except ValueError:
        return False

def geting_date_an_time_input():# TODO i can split it to get inputs but i will wair for now
    while True:
        date_str = input("Enter booking date (YYYY-MM-DD): ").strip()
        if validate_date_input(date_str) and validate_date_range(date_str, "00:00"):
            break
    while True:
        time_str = input("Enter start time (HH:MM): ").strip()
        if validate_time_input(time_str) and validate_time_range(time_str) and validate_date_range(date_str, time_str):
            break
    return date_str, time_str
