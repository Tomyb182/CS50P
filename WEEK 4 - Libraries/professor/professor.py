
import random


def main():
    level = get_level()
    operations = generate_integer(level)

    score = 0
    for operation, result in operations:
        tries = 0

        while tries < 3:
            try:
                user_answer = input(operation)
                if user_answer == str(result):
                    score += 1
                    break
                else:
                    tries += 1
                    print('EEE')
                    if tries == 3:
                        print(result)
                        break 
            except ValueError:
                tries += 1
                print('EEE')
                if tries == 3:
                    print(result)
                    break
                pass

    print(f'Score: {score}')



def get_level():
    while True:
        try:
            lvl = int(input('Level: '))
            if lvl == 1 or lvl == 2 or lvl == 3:
                break
        except ValueError:
            pass
    return lvl

def generate_integer(level):
    if level ==1:
        operations = []
        for _ in range(10):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            operation = f"{x} + {y} = "
            result = x + y
            operations.append((operation, result))
    elif level ==2:
        operations = []
        for _ in range(10):
            x = random.randint(10, 99)
            y = random.randint(10, 99)
            operation = f"{x} + {y} = "
            result = x + y
            operations.append((operation, result))
    elif level== 3:
        operations = []
        for _ in range(10):
            x = random.randint(100, 999)
            y = random.randint(100, 999)
            operation = f"{x} + {y} = "
            result = x + y
            operations.append((operation, result))

    return operations

if __name__ == "__main__":
    main()
