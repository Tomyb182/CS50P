def main():
    name = input('camelCase: ')
    snake_name = ''

    for letter in name:
        if letter.isupper():
            snake_name += '_' + letter.lower()
        else:
            snake_name+= letter
    print('snake_Case: ',snake_name)


if __name__ == '__maine__':
    main()


main()

