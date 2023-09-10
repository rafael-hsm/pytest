from app.upper_text import TextUpper


def test_text_to_uppercase():
    tu = TextUpper()
    text_ = tu.text_up("first text to test")
    
    return_expected = "FIRST TEXT TO TEST"

    assert text_ == return_expected
