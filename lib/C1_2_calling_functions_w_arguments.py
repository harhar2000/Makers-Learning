# == EXERCISES ==

# Purpose: checks if a string starts with the letter a
# Example:
#   Call:    starts_with_the_letter_a("apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Rock")
#   Returns: False
def starts_with_the_letter_a(string):
    if string[0] == 'a' or string[0] == 'A':
        return True
    return False

print(starts_with_the_letter_a("apple"))
print(starts_with_the_letter_a("Apple"))
print(starts_with_the_letter_a("Rock"))


# Purpose: checks if a string ends with the letter a
# Example:
#   Call:    ends_with_the_letter_a("Java")
#   Returns: True
#   Call:    ends_with_the_letter_a("JAVA")
#   Returns: True
#   Call:    ends_with_the_letter_a("Python")
#   Returns: False
def ends_with_the_letter_a(string):
    if string[-1] == 'a' or string[-1] == 'A':
        return True
    return False

print(ends_with_the_letter_a("Java"))
print(ends_with_the_letter_a("JAVA"))
print(ends_with_the_letter_a("Python"))


# Purpose: checks if a string contains the word hello
# Example:
#   Call:    contains_hello("hello world")
#   Returns: True
#   Call:    contains_hello("HELLO WORLD")
#   Returns: True
#   Call:    contains_hello("world")
#   Returns: False
def contains_hello(string):
    if "hello" in string or "HELLO" in string:
        return True
    return False

print(contains_hello("hello world"))
print(contains_hello("HELLO WORLD"))
print(contains_hello("world"))


# Purpose: replaces the word hello with the word goodbye
# Note: you don't need to worry about matching 'Hello' or 'HELLO' here
#       lowercase only is fine.
# Example:
#   Call:    substitute_hello_with_goodbye("hello folks")
#   Returns: "goodbye folks"
#   Call:    substitute_hello_with_goodbye("Hello folks")
#   Returns: "Hello folks"
def substitute_hello_with_goodbye(string):
    if "hello" in string:
        return "goodbye folks"
    return string
    
print(substitute_hello_with_goodbye("hello folks"))
print(substitute_hello_with_goodbye("Hello folks"))


# Purpose: removes the letter x from a string
# Example:
#   Call:    remove_x("xoxo")
#   Returns: "oo"
#   Call:    remove_x("OXO")
#   Returns: "OO"
def remove_x(string):
   return string.replace("x", "").replace("X", "")
        
print(remove_x("xoxo"))
print(remove_x("OXO"))


# Purpose: returns the first half of a string
# Example:
#   Call:    first_half("coding")
#   Returns: "cod"
# Note: you can assume the string will always have an even number of characters
def first_half(string):
    total = len(string)
    half = total //2
    return string[:half]

print(first_half("coding"))


# Purpose: returns the second half of a string
# Example:
#   Call:    second_half("coding")
#   Returns: "ing"
# Note: you can assume the string will always have an even number of characters
def second_half(string):
    total = len(string)
    half = total //2
    return string[half:]

print(second_half("coding"))