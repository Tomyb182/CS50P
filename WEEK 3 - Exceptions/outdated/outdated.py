
def main():
    while True:
        months_list=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
        try:
            date = input('Date: ')
            if '/' in date:
                month,day,year = date.split('/')
                month = int(month)
                year = int(year)
                day = int(day)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f'{year}-{month:02}-{day:02}')
                    break
            else:
                if ',' in date:
                    month_name, day, year = date.split(' ')

                    month = months_list.index(month_name) + 1

                    day = int(day.rstrip(','))
                    if  1 <= month <= 12 and 1 <= day <= 31:
                        print(f'{year}-{month:02}-{day:02}')
                        break
                pass

        except: ValueError
        pass


#El input ideal del usuario sera de MES/DIA/ANO
main()
