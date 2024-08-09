from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("hello, WORLD") == "hll, WRLD"
    assert shorten("23") == "23"
    assert shorten("CS50") == "CS50"
    assert shorten(",._-") == ",._-"


if __name__ == "__main__":
    main()
