
def main():

    answer = input("What is the Answer to the Great question of Life, the Universe and Everything? ").strip()

    if answer == '42':
        print ("yes")
    elif answer.lower() == 'forty two':
        print('yes')
    elif answer.lower() == 'forty-two':
        print('Yes')
    else:
        print('No')

main()
