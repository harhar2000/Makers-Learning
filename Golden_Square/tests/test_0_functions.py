# File: tests/test_add_five.py
from lib._0_functions import *

def test_add_five_returns_eight_for_three():
    result = add_five(3)
    assert result == 8

def test_greet_adds_name_to_string():
    result = greet("Harry")
    assert result == "Hello, Harry!"

def test_returns_correct_string():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_wrong_codeword_returns_correct_string():
    result = check_codeword("shoe")
    assert result == "WRONG!"

def test_begins_ends_correct():
    result = check_codeword("house")
    assert result == "Close, but nope." 

def test_char_len_is_string():
    result = report_length("stringIs8")
    assert result == "This string was 9 characters long."

def test_empty_str():
    result = report_length("")
    assert result == "This string was 0 characters long."