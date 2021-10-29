# Created by Marcin "Cozoob" Kozub 29.10.2021
import re

def get_num(arg):
    return int(arg[0:len(arg) - 1])


def validate_and_get_time(time_string):
    # the correct input is for example "7w 6h 5d"
    # which means that there is 7 weeks, 5 days
    # and 5 hours of time
    weeks, days, hours = 0, 0, 0

    try:
        weeks = re.search(r"[0-9]+w", time_string).group()
        weeks = get_num(weeks)
    except AttributeError:
        pass

    try:
        days = re.search(r"[0-9]+d", time_string).group()
        days = get_num(days)
    except AttributeError:
        pass

    try:
        hours = re.search(r"[0-9]+h", time_string).group()
        hours = get_num(hours)
    except AttributeError:
        pass

    if not 0 <= hours <= 24:
        hours = 0

    if not 0 <= days <= 31:
        days = 0

    return f"Weeks: {weeks}; Days: {days}; Hours: {hours}"

if __name__ == '__main__':
    print(validate_and_get_time("7w 5d 6h"))
    print(validate_and_get_time("23 t74ww h6hhh d5dd"))
    print(validate_and_get_time("783nmasdkarned8w90idasw9w 3h 5d"))