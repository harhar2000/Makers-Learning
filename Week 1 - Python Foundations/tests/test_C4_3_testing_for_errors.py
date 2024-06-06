import pytest
from lib.C4_3_testing_for_errors import *

def test_reminder():
    reminder = Reminder("Kay")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"

# There are three key differences above:

# We import pytest to check for errors.
# We use with pytest.raises(Exception) as e: to set up a section of the code where we expect error to occur and then be caught by pytest.
# We use str(e.value) to get the error message that was generated, and then assert it as correct one
    

def test_present_wrap():
    present = Present()
    content = "Toy"
    present.wrap(content)
    assert present.contents == content

def test_wrap_present_already_wrapped():
    present = Present()
    present.wrap("Toy")
    with pytest.raises(Exception) as e:
        present.wrap("Book")
    assert str(e.value) == "A contents has already been wrapped."

def test_unwrap_present():
    present = Present()
    content = "Toy"
    present.wrap(content)
    assert present.unwrap() == content

def test_unwrap_empty_present():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    assert str(e.value) == "No contents have been wrapped."



def test_passwordchecker_check_length():
    passwordchecker = PasswordChecker()
    assert passwordchecker.check("abcd1234") == True
    assert passwordchecker.check("longpassword123") == True
    try:
        passwordchecker.check("short")
        assert False, "Failed: Password with less than 8 characters should not be valid"
    except Exception as e:
        assert str(e) == "Invalid password, must be 8+ characters."