
def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if first(s) and second(s) and third(s) and fourth(s) and no_zero_first_number(s):
        return True
    else:
        return False

def no_zero_first_number(plate):
    # Busca el primer número en la placa
    for char in plate:
        if char.isdigit():
            # Verifica si el primer número no es '0'
            if char != '0':
                return True
            else:
                return False
    # Si no se encontró ningún número, la placa es válida
    return True


def fourth(x):
    numbers = '0123456789'
    found_non_number = False

    for char in reversed(x):
        if char not in numbers:
            found_non_number = True

        elif found_non_number:
            return False
    return True


def third(p):
    special = ['.', ' ', ':', ';', '"', '(', ')', '-', '_', '!', '?']
    for char in p:
        if char in special:
            return False
    return True


def second(o):
    if 2 <= len(o) <= 6:
        return True
    else:
        return False


def first(t):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in t[:2]:
        if char in numbers:
            return False
    return True



if __name__=="__main__":
    main()

#All vanity plates must start with at least two letters OK
#vanity plates may contain a maximum of 6 characters and a minimum of 2 characters OK
#Numbers cannot be used in the middle of a plate OK
#No periods, spaces, or punctuation marks are allowed. OK
# The first number used cannot be a ‘0’.

