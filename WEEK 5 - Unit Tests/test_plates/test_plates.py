from plates import is_valid



def main():
    test_is_valid()

def test_is_valid():
    assert is_valid("0th55") == False
    assert is_valid("4thb") == False
    assert is_valid("th 65") == False
    assert is_valid("tg55h") == False
    assert is_valid("rgt5") == True
    assert is_valid("a") == False
    assert is_valid("222") == False
    assert is_valid("CS50")== True
    assert is_valid("flf") == True
    assert is_valid("Hello, World")== False
    assert is_valid("33464")== False
    assert is_valid("")==False
    assert is_valid("cs05")==False
#All vanity plates must start with at least two letters OK <--------------------------
#No periods, spaces, or punctuation marks are allowed. OK<--------------------------
# The first number used cannot be a ‘0’.<--------------------------
#vanity plates may contain a maximum of 6 characters and a minimum of 2 characters OK<--------------------------
#Numbers cannot be used in the middle of a plate OK



