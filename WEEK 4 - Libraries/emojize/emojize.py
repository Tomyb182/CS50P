import emoji

def main():

    user_input = str(input('Input: '))

    print(emoji.emojize(user_input, language='alias'))



if __name__ == "__main__":
    main()
