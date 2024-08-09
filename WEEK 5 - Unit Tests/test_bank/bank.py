

def main():
    greet = str(input('Greeting: ')).strip().lower()
    print(value(greet).lower())

def value(greeting2):
    greeting = greeting2.lower()
    if greeting.startswith('hello'):
        return 0
    elif greeting.startswith('h'):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

# 0 si esa cadena comienza con "hello"
# 20 si esa cadena comienza con una "h" (pero no "hello")
# o 100 de lo contrario

