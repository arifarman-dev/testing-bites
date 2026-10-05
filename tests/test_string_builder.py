from lib.string_builder import *

def test_string_builder_returns_4():
    test_string_builder = StringBuilder()
    test_string_builder.add("Arif")
    test_string_builder_size = test_string_builder.size()
    assert test_string_builder_size == 4

def test_string_builder_returns_string():
    test_string_builder = StringBuilder()
    test_string_builder.add("Arif")
    test_string_builder_output = test_string_builder.output()
    assert test_string_builder_output == "Arif"