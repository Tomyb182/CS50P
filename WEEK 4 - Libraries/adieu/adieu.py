import inflect
p = inflect.engine()

def main():
    name = []
    while True:
        try:
            user_input = input('')

            if not user_input.strip():
                break

            name.append(user_input.strip())
        except EOFError:
            break

    if len(name) == 1:
        print('Adieu, adieu, to', name[0])
    elif len(name) > 1:
        print('Adieu, adieu, to',(p.join(name)))
    else:
        pass
if __name__ == "__main__":
    main()












'''
import inflect
p = inflect.engine()

def main():
    name = []
        try:
            user_input = input('')

            #if user_input.strip() == "":
                #break
            name.append(user_input.strip())

            if len(name) == 1:
                print('Adieu, adieu, to', name[0])
                break
            else:
                print('Adieu, adieu, to',(p. join(name)))
                break
        except EOFError:
            pass


main()
'''
