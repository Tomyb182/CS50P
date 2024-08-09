


def main():

    words=input('Input: ')
    print(shorten(words))

def shorten(word):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    retur = ''

    for letter in word:
        if letter not in vowels:
            retur += letter
    return retur

if __name__ == "__main__":
    main()
