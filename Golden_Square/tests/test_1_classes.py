from lib._1_classes import *

def test_reminds_user_todo_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"


def test_count_reporter():
    counter = Counter()
    counter.add(4)
    counter.add(4)
    result = counter.report()
    assert result == "Counted to 8 so far."


def test_initial_output():
    sb = StringBuilder()
    sb.add("")
    result = sb.output()
    assert result == ""

def test_initial_size():
    sb = StringBuilder()
    sb.add("")
    result = sb.size()
    assert result == 0

def test_add_string():
    sb = StringBuilder()
    sb.add("Hello")
    result = sb.output()
    assert result == "Hello"

def test_add_multiple_strings():
    sb = StringBuilder()
    sb.add("Hello")
    sb.add("John")
    result = sb.output()
    assert result == "HelloJohn"


def test_initial_format():
    pass

def add_single_gratitude():
    pass

def add_multiple_gratitudes():
    pass