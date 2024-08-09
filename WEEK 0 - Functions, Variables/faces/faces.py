def main():
    a = str(input('Insert a frase: '))

    b= convert(a)

    print(b)

def convert(string):
    result_string = string.replace(':)', '🙂').replace(':(', '🙁')

    return result_string


main()


