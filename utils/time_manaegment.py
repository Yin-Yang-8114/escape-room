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

def validate_date_range(date_str):
    try:
        dateObject = datetime.strptime(date_str, '%Y-%m-%d').date()
        if dateObject < date.today():
            return False    
        else:
            return True
    except ValueError:
        return True


def validating_room_avalability():
    pass


