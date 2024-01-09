from lib.C4_2_testing_classes_with_equality import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"

def test_reminds_the_latest_task():
    reminder = Reminder("Alex")
    reminder.remind_me_to("Buy groceries")
    reminder.remind_me_to("Call mum")
    result = reminder.remind()
    assert result == "Call mum, Alex!"

def test_reminds_with_special_characters():
    reminder = Reminder("Zoë123")
    reminder.remind_me_to("Review the project @ 3pm")
    result = reminder.remind()
    assert result == "Review the project @ 3pm, Zoë123!"



def test_counter_initialises_count_at_zero():
    counter = Counter()
    counter.add(0)
    result = counter.report()
    assert result == "Counted to 0 so far."

def test_counter_adds_correctly():
    counter = Counter()
    counter.add(5)
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 10 so far."

def test_counter_returns_correct_string():
    counter = Counter()
    counter.add(546)
    result = counter.report()
    assert result == "Counted to 546 so far."



def test_stringbuilder_initialises_empty_string():
    stringbuilder = StringBuilder()
    result = stringbuilder.output()
    assert result == ""
    

def test_stringbuidler_concatenates_correctly():
    stringbuilder = StringBuilder()
    stringbuilder.add("Hello, ")
    stringbuilder.add("Bob")
    result = stringbuilder.output()
    assert result == "Hello, Bob"

def test_stringbuilder_returns_correct_length_of_string():
    stringbuilder = StringBuilder()
    stringbuilder.add("Hello")
    result = stringbuilder.size()
    assert result == 5

def test_stringbuilder_returns_correct_output_string():
    stringbuilder = StringBuilder()
    stringbuilder.add("Hello, ")
    stringbuilder.add("world!")
    expected_output = "Hello, world!"
    assert stringbuilder.output() == expected_output
    


def test_gratitudes_initialised_empty_list():
    gratitudes = Gratitudes()
    result = gratitudes.format()
    assert result == "Be grateful for: "
    
def test_gratitudes_append_gratitude_correctly():
    gratitudes = Gratitudes()
    gratitudes.add("cheese")
    gratitudes.add("biscuits")
    result = gratitudes.format()
    assert result == "Be grateful for: cheese, biscuits"

def test_gratitudes_return_format_correctly():
    gratitudes = Gratitudes()
    gratitudes.add("health")
    gratitudes.add("family")
    gratitudes.add("friends")
    expected_output = "Be grateful for: health, family, friends"
    assert gratitudes.format() == expected_output