import sys
from pyfiglet import Figlet

figlet = Figlet()

def main():
    if len(sys.argv) == 1:
        user_input = input('Input: ')
        print("Output: ", figlet.renderText(user_input))

    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font_name = sys.argv[2]
        if font_name in figlet.getFonts():
            figlet.setFont(font=font_name)
            user_input = input('Input: ')
            print("Output: \n" + figlet.renderText(user_input))
        else:
            sys.exit("Error: Font not found")

    else:
        sys.exit("Usage: python script.py [-f/--font fontname]")

if __name__ == "__main__":
    main()


#print(figlet.getFonts())
#sys.argv[]
