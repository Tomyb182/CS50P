from datetime import date, timedelta
import sys
import re
import operator
import inflect

p = inflect.engine()

def main():
    inputt = input('Date of Birth: ')

    user_date = birthdate(inputt)
    today_date = date.today()

    difference = operator.__sub__(today_date, user_date) #Difference es una objeto timedelta
    total_minutes = round((difference.total_seconds())/60)
    words = p.number_to_words(total_minutes, andword="")
    wordsC = words.capitalize()
    print(f'{wordsC} minutes')



def birthdate(s):
    match = re.match(r'^\d{4}-\d{2}-\d{2}$',s)
    if match:
        try:
            # Convert to a date objet
            birth_date = date.fromisoformat(s)
            return birth_date

        except ValueError:
            sys.exit('Invalid date')
    else:
        sys.exit('Invalid date')


if __name__ == "__main__":
    main()





