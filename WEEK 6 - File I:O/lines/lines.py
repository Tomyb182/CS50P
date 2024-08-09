import sys

def main():
    check_input()
    try:
        file = open(sys.argv[1],"r")
        lines = file.readlines()
        contador = 0
        for line in lines:
            if check_line(line) == False:
                contador+=1
            else:
                contador+=0

    except FileNotFoundError:
        sys.exit("File does not exists")
    print(contador)

def check_input():

    if len(sys.argv)>2:
        sys.exit('Too many command-line arguments')
    if len(sys.argv)<2:
        sys.exit('Too few command-line arguments')

    if ".py" not in sys.argv[1]:
        sys.exit('Not a Python File')


def check_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False

if __name__=="__main__":
    main()

