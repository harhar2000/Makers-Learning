from lib._4_test_drive_single_class import *


def test_initialisation_with_valid_title_and_contents():
    title = "My Diary Entry"
    contents = "Today I learned something new."
    entry = DiaryEntry(title, contents)
    assert entry.title == title
    assert entry.contents == contents

def test_format_method_with_simple_title_and_contents():
    title = "My Diary Entry"
    contents = "Today I learned something new."
    entry = DiaryEntry(title, contents)
    assert entry.format() == "My Diary Entry: Today I learned something new."


def test_count_words_with_simple_contents():
    title = "Hello"
    contents = "This string is six words long"
    entry = DiaryEntry(title, contents)
    assert entry.count_words() == 6


def test_count_words_with_empty_contents():
    title = ""
    contents = " "
    entry = DiaryEntry(title, contents)
    assert entry.count_words() == 0

def test_count_words_with_multiple_spaces_and_newlines():
    title = "Test Entry"
    contents = "Today    I learned\nsomething new."
    entry = DiaryEntry(title, contents)
    assert entry.count_words() == 5


def test_count_words_with_special_characters():
    title = "Test @ Entry"
    contents = "Today    I learned\nsomething new! #new."
    entry = DiaryEntry(title, contents)
    assert entry.count_words() == 6


def test_reading_time_with_simple_contents_and_standard_wpm():
    title = "hello"
    contents = "word " * 200
    entry = DiaryEntry(title, contents)
    wpm = 200
    assert entry.reading_time(wpm) == 1


def test_reading_time_with_empty_contents():
    title = "hello"
    contents = " " * 200
    entry = DiaryEntry(title, contents)
    wpm = 200
    assert entry.reading_time(wpm) == 0


def test_reading_time_with_high_wpm():
    title = "hello"
    contents = "word " * 200
    entry = DiaryEntry(title, contents)
    wpm = 500
    assert entry.reading_time(wpm) == 1

def test_reading_chunk_with_simple_contents_and_standard_wpm_and_minutes():
    title = "hello"
    contents = "word " * 200 
    wpm = 200
    minutes = 1
    entry = DiaryEntry(title, contents)
    expected_chunk = "word " * 200  # Since wpm is 200 and minutes is 1, it returns all 200 words
    assert entry.reading_chunk(wpm, minutes).strip() == expected_chunk.strip()




def test_checks_capital_first_letter_and_ending_full_stop():
    text = "Hello."
    grammar = GrammarStats()
    assert grammar.check(text) == True



def test_percentage_good_no_texts_checked():
    grammar = GrammarStats()
    assert grammar.percentage_good() == 0

def test_percentage_good_all_texts_valid():
    grammar = GrammarStats()
    grammar.check("Hello.")
    grammar.check("World.")
    grammar.check("This is a valid text.")
    assert grammar.percentage_good() == 100

def test_percentage_good_no_texts_valid():
    grammar = GrammarStats()
    grammar.check("hello")
    grammar.check("world")
    grammar.check("this is not valid text")
    assert grammar.percentage_good() == 0

def test_percentage_good_some_texts_valid():
    grammar = GrammarStats()
    grammar.check("Hello.")
    grammar.check("world")
    grammar.check("This is valid.")
    grammar.check("this is not")
    assert grammar.percentage_good() == 50

def test_percentage_good_initially_no_texts_then_valid_texts():
    grammar = GrammarStats()
    assert grammar.percentage_good() == 0
    grammar.check("Hello.")
    grammar.check("World.")
    assert grammar.percentage_good() == 100

def test_percentage_good_initially_no_texts_then_invalid_texts():
    grammar = GrammarStats()
    assert grammar.percentage_good() == 0
    grammar.check("hello")
    grammar.check("world")
    assert grammar.percentage_good() == 0

def test_percentage_good_mixed_texts_over_time():
    grammar = GrammarStats()
    assert grammar.percentage_good() == 0
    grammar.check("Hello.")
    assert grammar.percentage_good() == 100
    grammar.check("world")
    assert grammar.percentage_good() == 50
    grammar.check("This is valid.")
    assert grammar.percentage_good() == 66
    grammar.check("this is not")
    assert grammar.percentage_good() == 50
