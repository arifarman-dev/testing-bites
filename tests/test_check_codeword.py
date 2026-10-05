from lib.check_codeword import *

def test_check_codeword_returns_correct():
    password = check_codeword("horse")
    assert password == "Correct! Come in."

def test_check_codeword_returns_close():
    password = check_codeword("hose")
    assert password == "Close, but nope."

def test_check_codeword_returns_wrong():
    password = check_codeword("cat")
    assert password == "WRONG!"