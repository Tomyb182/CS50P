def main():
    inputt = input('Fraction: ')
    tablero=convert(inputt)

    print(gauge(tablero))

def convert(fraction):
    x, y = fraction.split('/')
    num = int(x)
    den = int(y)

    if not (x.isdigit() and y.isdigit()):
        raise ValueError

    if den == 0:
        raise ZeroDivisionError

    if num > den:
        raise ValueError

    return round(num / den * 100)



def gauge(percentage):

    if 1<percentage<99:
        return f"{percentage}%"
    elif percentage >=99:
        return 'F'
    elif percentage <=1:
        return 'E'


if __name__ == "__main__":
    main()


'''
 If X and/or Y is not an integer, or if X is greater than Y,
   then convert should raise a ValueError.
If Y is 0, then convert should raise a ZeroDivisionError.
'''








'''
def main():
    while True:
        try:
            gauge = input('Fraction: ')
            x, y = gauge.split('/')
            num = int(x)
            den = int(y)

            if den >= num:
                result = round(num / den * 100)

                if 1<result<99:
                    print(f'{result}%')
                elif result >=99:
                    print('F')
                elif result <=1:
                    print('E')
                break
        except (ValueError, ZeroDivisionError) as error:
            pass

main()



    '''
