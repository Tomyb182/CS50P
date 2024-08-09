
def main():
    time = str(input('What time is it '))

    real_time = round(convert(time),2)

    if 7.0<= real_time <= 8.0:
        print('breakfast time')
    elif 12.0<= real_time <=13.0:
        print('lunch time')
    elif 18.0<= real_time <=19.0:
        print('dinner time')
    else:
        pass



def convert(t):
    hours, minutes = t.split(":")
    minutes = float(minutes)
    hours = float(hours)

    real_time = hours + minutes / 60
    return round(real_time, 2)




if __name__ == "__main__":
        main()


