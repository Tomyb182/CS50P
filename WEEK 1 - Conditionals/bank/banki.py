#If the greeting starts with “hello”, output $0
#If the greeting starts with an “h” (but not “hello”), output $20
#Otherwise, output $100.

#str.startswith(prefix[, start[, end]])

def main():
    greet = input('Greeting: ').strip()

    if not greet.startswith('H'):
        print('$100')
    elif greet.startswith('Hello'):
        print('$0')
    else:
        print('$20')



main()
