from lib.gratitudes import *

def test_gratitudes_appends_to_list():
    test_gratitudes = Gratitudes()
    test_gratitudes.add("Health")
    test_gratitudes.add("Job")
    assert len(test_gratitudes.gratitudes) == 2

def test_gratitudes_format():
    test_gratitudes = Gratitudes()
    test_gratitudes.add("Health")
    test_gratitudes.add("Job")
    assert test_gratitudes.format() == "Be grateful for: Health, Job"