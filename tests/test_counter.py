from lib.counter import *

def test_count_from_0_to_5():
    test_counter = Counter()
    test_counter.add(5)
    
    assert test_counter.report() == "Counted to 5 so far."