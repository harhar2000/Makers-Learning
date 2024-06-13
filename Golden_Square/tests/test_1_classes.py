from lib._1_classes import *

def test_reminds_the_user_to_do_a_task():
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

def test_string_count():
    sb = StringBuilder()
    sb.add("hello")
    result = sb.size()
    assert result == 5


def test_add_single_gratitude():
    gt = Gratitudes()
    gt.add("pets")
    result = gt.format()
    assert result == "Be grateful for: pets"


def test_add_mulitple_gratitudes():
    gt = Gratitudes()
    gt.add("pets")
    gt.add("cheese")
    result = gt.format()
    assert result == "Be grateful for: pets, cheese"