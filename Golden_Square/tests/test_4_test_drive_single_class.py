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