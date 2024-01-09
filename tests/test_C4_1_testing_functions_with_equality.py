from lib.C4_1_testing_functions_with_equality import *

def test_add_five_returns_eight_for_three():
    result = add_five(3)
    assert result == 8
    
    
def test_greet_returns_name_after_hello():
    result = greet("Harry")
    assert result == "Hello, Harry!"


def test_check_codeword_horse_returns_correct_string():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_codeword_first_char_is_h_and_last_letter_is_e():
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_check_codeword_returns_wrong_when_other_tests_are_invalid():
    result = check_codeword("hello")
    assert result == "WRONG!"


def test_report_length_returns_correct_string():
    assert report_length("Hello, world!") == "This string was 13 characters long."
    assert report_length("") == "This string was 0 characters long."
    assert report_length("   ") == "This string was 3 characters long."
    assert report_length("12345") == "This string was 5 characters long."
    assert report_length("!@#$%") == "This string was 5 characters long."

