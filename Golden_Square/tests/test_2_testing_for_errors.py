from os import error
from lib._2_testing_for_errors import * 
import pytest # <-------   

def test_reminder():
    # reminder = Reminder("Kay")
    # result = reminder.remind()
    # assert result == "No reminder set!"


    # Will return Error: "Exception: No reminder set!"
    # To test errors are thrown properly, adapt your approach

    reminder = Reminder("Kay")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"


# Import pytest to check for errors.
# Use with pytest.raises(Exception) as e: to set up section of code where we expect error to occur and be caught by pytest.
# Use str(e.value) to get generated error message and then assert it is correct one.


def test_initial_contents_is_none():
    present = Present()
    assert present.contents == None

def test_wrap_sets_contents_correctly():
    present = Present()
    result = present.wrap("gift")
    assert present.contents == "gift" 

def test_wrap_raises_exception_if_already_wrapped():
    present = Present()
    present.wrap("Toy")
    with pytest.raises(Exception) as e:
        present.wrap("Book")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_unwrap_returns_contents():
    present = Present()
    present.wrap("toy")
    contents = present.unwrap()
    assert contents == "toy"

def test_unwrap_raises_exception_if_no_contents():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_unwrap_after_wrap_returns_same_contents():
    present = Present()
    present.wrap("chocolate")
    contents = present.unwrap()
    assert contents == "chocolate"