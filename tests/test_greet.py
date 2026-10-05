from lib.greet import *

def test_greet_return_hello_name():
    greeting = greet("Arif")
    assert greeting == "Hello, Arif!"