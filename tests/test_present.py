import pytest
from lib.present import *

def test_present_wrap():
    test_present = Present()
    test_present.wrap("Lynx Africa")
    with pytest.raises(Exception) as e:
        test_present.wrap("Toilet roll")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_present_unwrap():
    test_present = Present()
    with pytest.raises(Exception) as e:
        test_present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."