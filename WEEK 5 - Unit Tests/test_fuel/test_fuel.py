from fuel import convert
from fuel import gauge
import pytest

def main():
    test_convert_gauge()
    zero_div()
    value_err()


def zero_div():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def value_err():
    with pytest.raises(ValueError):
        convert('cat/dog')


def test_convert_gauge():
    assert convert('3/4') == 75 and gauge(75) == '75%'
    assert convert('1/100') == 1 and gauge(1)== 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'

    with pytest.raises(ValueError):
        convert('101/100')  
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('cat/dog')



if __name__ == "__main__":
    main()
