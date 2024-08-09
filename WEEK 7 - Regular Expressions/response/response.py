from validator_collection import validators, errors

def main():
    try:
        user_email=input("What's your email address? ")

        if validators.email(user_email):
            print('Valid')

    except errors.InvalidEmailError:
        print('Invalid')

if __name__=="__main__":
    main()

