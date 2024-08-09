import sys
import csv

def main():
    check_input()
    students = function_to_read()
    convert_and_write(students)
print

def convert_and_write(students):
    with open(sys.argv[2], 'w') as newfile:
        writer = csv.DictWriter(newfile, fieldnames=['first', 'last', 'house'])
        writer.writerow({"first": "first", "last": "last", "house": "house"})


        for student in students:
            writer.writerow({'first': student['first'] , 'last': student['last'] , 'house':student['house']})


def function_to_read():
    try:
        students = []
        with open(sys.argv[1], 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                split_name = row['name'].split(',')
                students.append({'first': split_name[1].lstrip(), 'last': split_name[0], 'house': row['house']})
        return students
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')

def check_input():

    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) >3:
        sys.exit('Too many command-line arguments')
    if '.csv' not in sys.argv[1]:
        sys.exit(f'Could not read {sys.argv[1]}')


if __name__=="__main__":
    main()

