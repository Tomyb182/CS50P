import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    #CHECK INPUT FORMAT
    check = re.search(r'^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$', s)
    if check:
        partes = check.groups()
        if int(partes[1]) > 12 or int(partes[5]) >12:
            raise ValueError
        first_time = format_eu(partes[1],partes[2],partes[3])
        second_time = format_eu(partes[5],partes[6],partes[7])
        return first_time + ' to ' + second_time
    else:
        raise ValueError


def format_eu(h,m, amYpm):
    if amYpm == 'PM':
        if int(h)==12:
            hour_eu= 12
        else:
            hour_eu = int(h) + 12
    else:
        if int(h) == 12:
            hour_eu = 0
        else:
            hour_eu = int(h)
    if m == None:
        minute_eu = ':00'
        time_eu = f'{hour_eu:02}' + minute_eu
    else:
        time_eu = f'{hour_eu:02}' + ':' + m

    return time_eu

if __name__ == "__main__":
    main()

# Input examples:
# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9 AM to 5:30 PM

