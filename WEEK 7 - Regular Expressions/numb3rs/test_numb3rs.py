from numb3rs import validate

def main():
    test_validate()

def test_validate():
    assert validate('1.1.1.1') == True
    assert validate('0.0.0.0') == True
    assert validate('255.255.255.255') == True
    assert validate('23.124.168.44') == True
    assert validate('cat') == False
    assert validate('2..14.') == False
    assert validate('75.456.76.65') == False
    assert validate('192.168.1.1.1') == False
