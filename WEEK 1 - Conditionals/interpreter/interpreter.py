
#z can be + - / *

def main():
    expression = input('Expression: ')
    x,y,z = expression.split(" ")

    x=float(x)
    z=float(z)

    if y == '+' :
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    else:
        result = x/z


    print(result)

    #print(f'{x}{y}{z}')


main()
