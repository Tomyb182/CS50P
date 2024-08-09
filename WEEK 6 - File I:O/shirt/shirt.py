import sys
import os.path
from PIL import Image, ImageOps

def main():
    check_input()
    try:
        shirt = Image.open("shirt.png")
        muppet =Image.open(sys.argv[1])

        muppetFinal = ImageOps.fit(muppet, shirt.size)
        muppetFinal.paste(shirt, shirt)
        muppetFinal.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit('File not found')

def check_input():
    formats = ['.jpg', 'jpeg','png']
    if len(sys.argv)> 3:
        sys.exit('Too many command-line arguments')
    if len(sys.argv)< 3:
        sys.exit('Too few command-line arguments')

    file1_extension = os.path.splitext(sys.argv[1])[1].lower()
    file2_extension = os.path.splitext(sys.argv[2])[1].lower()

    if file1_extension not in formats or file2_extension not in formats:
        sys.exit('Invalid input')

    if file1_extension != file2_extension:
        sys.exit('Both files must have the same extension')


if __name__ == "__main__":
    main()
