from lib.C1_2_calling_functions_w_arguments import *

def test_starts_with_the_letter_a():
    assert starts_with_the_letter_a("Apple") == True
    assert starts_with_the_letter_a("a") == True
    assert starts_with_the_letter_a("JavaScript") == False


def test_ends_with_the_letter_a():
    assert ends_with_the_letter_a("Java") == True
    assert ends_with_the_letter_a("JAVA") == True
    assert ends_with_the_letter_a("Server") == False


def test_contains_hello():
    assert contains_hello("hello world") == True
    assert contains_hello("HELLO WORLD") == True
    assert contains_hello("world") == False


def test_substitute_hello_with_goodbye():
    assert substitute_hello_with_goodbye("hello folks") == "goodbye folks"
    assert substitute_hello_with_goodbye("Hello folks") == "Hello folks"


def test_remove_x():
    assert remove_x("xoxo") == "oo"
    assert remove_x("OXO CUBE") == "OO CUBE"
    assert remove_x("xx") == ""
    assert remove_x("x") == ""
    assert remove_x("") == ""


def test_first_half():
    assert first_half("Coding") == "Cod"
    assert first_half("sunburnt") == "sunb"


def test_second_half():
    assert second_half("Sampling") == "ling"
    assert second_half("Headlamp") == "lamp"