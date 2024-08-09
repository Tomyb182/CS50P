import random

while True:
    try:
        lvl = int(input('Level: '))
        if lvl > 0:
            break
    except ValueError:
            pass
random_number = random.randint(1,lvl)

while True:
    try:
        guessed = int(input('Guess: '))
        if guessed > random_number:
            print('Too large!')
        elif guessed < random_number:
            print('Too small!')
        else:
            print("Just right!")
            break
    except ValueError:
            pass



