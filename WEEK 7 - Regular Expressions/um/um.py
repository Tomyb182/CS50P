import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    counter = 0
    coincidence = re.findall(r'\bum\b',s,re.IGNORECASE)
    for match in coincidence:
        if coincidence:
            counter +=1

    return counter


if __name__ == "__main__":
    main()
