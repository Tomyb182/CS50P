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





