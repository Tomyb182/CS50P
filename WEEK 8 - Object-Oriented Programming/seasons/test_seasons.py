from seasons import birthdate
import pytest
import datetime
def main():
    test_birthdate()

def test_birthdate():
    expected_date = datetime.date(1999, 2, 2)
    assert birthdate('1999-02-02') == expected_date

