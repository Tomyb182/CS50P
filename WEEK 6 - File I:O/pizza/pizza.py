import sys
import csv
from tabulate import tabulate


def main():
    check_input()
    table=[]

    try:
        with open(sys.argv[1],'r') as file:
            reader  = csv.reader(file)
            headers = next(reader)

            for row in reader:
                table.append(row)

    except(FileNotFoundError):
        sys.exit('File does not exists')

    print(tabulate(table, headers = headers , tablefmt="grid"))

# DONE-------------------------------------------------
def check_input():
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if '.csv' not in sys.argv[1]:
        sys.exit('Not a CSV file')
# DONE-------------------------------------------------


if __name__=="__main__":
    main()
