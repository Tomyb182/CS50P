import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):

    link= re.search(r'src="([^"]+youtube\.com/embed/[^"]+)',s)
    if link:
        incomplete_url = link.group(1)
        incomplete_url = incomplete_url.replace('/embed','')
        incomplete_url = incomplete_url.replace('http://', 'https://')
        incomplete_url = incomplete_url.replace('youtube.com','youtu.be')
        incomplete_url = incomplete_url.replace('www.','')
        return incomplete_url
    else:
        return None




if __name__ == "__main__":
    main()


#Input example:
#<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

