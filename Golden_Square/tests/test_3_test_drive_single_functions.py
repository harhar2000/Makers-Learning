from lib._3_test_drive_single_functions import *


# leap_year = True
# non_leap_year = False

# if years % 400 == 0, years == True
# if years % 100 == 0 and years % 400 != 0, years == False
# if years % 4 == 0 and years % 100 != 0, years == True
# if years % 4 =! 0, years == False

# Ask about input validation, what needs to be validated
# Describe thought process before writing - don't pseudocode too quickly
# Double check rules after writing pseudocode 
# test for != 0 instead of = 1
# Say what thinking for debugging, so thought process is clear 
# Write one test then try and pass instead of all, comment out others. to focus on the one 
# Read error messages in detail
# More accurate variable names


def test_zero_returns():
    result = leap_year(0)   
    assert result == False

    # with pytest.raises(Exception) as e:
    # error_message = str(e.value)
    # assert error_message == "enter valid number!"

def tests_characters():
    result = leap_year("as")
    assert result == False

    # with pytest.raises(Exception) as e:
    # error_message = str(e.value)
    # assert error_message == "Input must be a integer"

def test_negative_numbers():
    result = leap_year(-2000)
    assert result == True

def test_for_leap_year_divisible_by_400():
    result = leap_year(2000)
    assert result == True

def test_for_leap_year_divisible_by_100_and_not_400_equals_false_0():
    result = leap_year(1700)
    assert result == False

def test_for_leap_year_divisible_by_100_and_not_400_equals_false_1():
    result = leap_year(1800)
    assert result == False

def test_for_leap_year_divisible_by_100_and_not_400_equals_false_2():
    result = leap_year(1900)
    assert result == False

def test_for_leap_year_divisible_by_100_and_not_400_equals_false_fails_correctly():
    result = leap_year(1901)
    assert result == False

def test_for_leap_year_divisible_by_4_but_not_divisible_by_100_equals_true_0():
    result = leap_year(2004)
    assert result == True

def test_for_leap_year_divisible_by_4_but_not_divisible_by_100_equals_true_1():
    result = leap_year(2008)
    assert result == True

def test_for_leap_year_divisible_by_4_but_not_divisible_by_100_equals_true_2():
    result = leap_year(2012)
    assert result == True

def test_for_leap_year_divisible_by_4_but_not_divisible_by_100_equals_true_fails_correclty():
    result = leap_year(2005)
    assert result == False

def test_for_leap_year_divisible_by_4_equals_false_0():
    result = leap_year(2009)
    assert result == False

def test_for_leap_year_divisible_by_4_equals_false_1():
    result = leap_year(2010)
    assert result == False

def test_for_leap_year_divisible_by_4_equals_false_2():
    result = leap_year(2011)
    assert result == False

def test_for_leap_year_divisible_by_4_equals_false_fails_correctly():
    result = leap_year(2008)
    assert result == True




def test_make_snippet_returns_first_five_words():
    result = make_snippet("one two three four five six")
    assert result == "one two three four five..."

def test_make_snippet_returns_first_five_words():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"

def test_count_words_counts_words():
    result = count_words("There are five words here")
    assert result == 5


def test_estimate_reading_time():
    text = "word " * 200
    result = estimate_reading_time(text)
    assert result == 1


def test_camel_case_and_ends_with_punctual():
    result = put_text_in_capital_and_end_punctually("Hello!")
    assert result == True