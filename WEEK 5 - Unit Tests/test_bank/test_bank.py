from bank import value

def main():
    test_value()

def test_value():
    assert value("hello") == 0
    assert value("what’s up") == 100
    assert value("hnothing") == 20
    assert value("Hello") == 0
    assert value("What’s up") == 100
    assert value("Hnothing") == 20



if __name__=="__main__":
    main()
