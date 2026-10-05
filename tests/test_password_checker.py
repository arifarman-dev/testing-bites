import pytest
from lib.password_checker import *

def test_password_checker_raises_error():
    test_password = PasswordChecker()
    with pytest.raises(Exception) as e:
        test_password.check("word")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_password_checker_does_not_raise_error():
    test_password = PasswordChecker()
    result = test_password.check("password")
    assert result == True