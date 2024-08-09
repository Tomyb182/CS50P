def main():
    words=str(input('Input: '))
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    retur = ''


    for letter in words:
        if letter in vowels:
            letter=''
        else:
            retur+= letter

    print('Output: ', retur)


main()

