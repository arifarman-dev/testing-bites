from lib.report_length import report_length

def test_report_length_returns_4():
    string = report_length("Arif")
    assert string == "This string was 4 characters long."

def test_report_length_returns_6():
    string = report_length("Makers")
    assert string == "This string was 6 characters long."