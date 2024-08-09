#E = M *c**2, this is the formula

def main():
    mass = int(input('m: '))

    E = convertion(mass)
    print('E: ', E)



def convertion(kilos):
    joules = kilos * 300000000**2

    return joules


main()
