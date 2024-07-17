# # Purpose: return the string uppercase
# # Example:
# #   Call:    block_caps_a_string("hello world")
# #   Returns: "HELLO WORLD"
# from stat import FILE_ATTRIBUTE_SPARSE_FILE


# def block_caps_a_string(string):
#     return string.upper()

# print(block_caps_a_string("hello world"))

# # Purpose: return the string lowercase
# # Example:
# #   Call:    lower_case_a_string("HELLO WORLD")
# #   Returns: "hello world"
# def lower_case_a_string(string):
#     return string.lower()

# print(lower_case_a_string("HELLO WORLD"))


# # Purpose: return the length of the string
# # Example:
# #   Call:    length_of_a_string("hello")
# #   Returns: 5
# def length_of_a_string(string):
#     return len(string)

# print(length_of_a_string("hello"))


# # Purpose: return the string reversed
# # Example:
# #   Call:    reverse_a_string("hello")
# #   Returns: "olleh"
# def reverse_a_string(string):
#     return string[::-1]

# print(reverse_a_string("hello"))

# # Purpose: return the string with uppercase swapped to lowercase and vice versa
# # Example:
# #   Call:    swap_the_case_of_a_string("Hello World")
# #   Returns: "hELLO wORLD"
# def swap_the_case_of_a_string(string):
#     return string.swapcase()

# print(swap_the_case_of_a_string("Hello World"))


# # Purpose: checks if the number given is odd
# # Example:
# #   Call:    is_integer_odd(1)
# #   Returns: True
# #   Call:    is_integer_odd(2)
# #   Returns: False
# def is_integer_odd(integer):
#     if integer % 2 == 1:
#         return True
#     else: 
#         return False

# print(is_integer_odd(1)) 
# print(is_integer_odd(2))  


# # Purpose: checks if the number given is even
# # Example:
# #   Call:    is_integer_even(1)
# #   Returns: False
# #   Call:    is_integer_even(2)
# #   Returns: True
# def is_integer_even(integer):
#    if integer % 2 == 0:
#        return True
#    else: 
#         return False

# print(is_integer_even(1))
# print(is_integer_even(2))

# # Purpose: converts an integer to a float
# # Example:
# #   Call:    integer_to_float(1)
# #   Returns: 1.0
# def integer_to_float(integer):
#     return float(integer)

# print(integer_to_float(1))

# # Purpose: converts an integer to a string
# # Example:
# #   Call:    integer_to_string(1)
# #   Returns: "1"
# def integer_to_string(integer):
#     return str(integer)

# print(integer_to_string(1))

# # Purpose: returns the integer one lower than the one given
# # Example:
# #   Call:    return_one_lower(4)
# #   Returns: 3
# def return_one_lower(integer):
#     return integer - 1

# print(return_one_lower(4))

# # Purpose: returns the integer one higher than the one given
# # Example:
# #   Call:    return_one_higher(4)
# #   Returns: 5
# def return_one_higher(integer):
#     return integer + 1

# print(return_one_higher(4))

# # Purpose: rounds a float up to the nearest integer
# # Example:
# #   Call:    round_up(4.5)
# #   Returns: 5
# def round_up(float):
#     if float == int(float):
#         return int(float)
#     return int(float) + 1

# print(round_up(4.5))


# # Purpose: rounds a float down to the nearest integer
# # Example:
# #   Call:    round_down(4.5)
# #   Returns: 4
# def round_down(float):
#     if float == int(float):
#         return int(float)
#     return int(float) 

# print(round_down(4.5))



# # Purpose: converts a float to a string
# # Example:
# #   Call:    float_to_string(1.0)
# #   Returns: "1.0"
# def float_to_string(float):
#     return str(float)

# print(float_to_string(1.0))


# # Purpose: converts a float to an integer
# # Example:
# #   Call:    float_to_integer(1.0)
# #   Returns: 1
# def float_to_integer(float):
#     return int(float)

# print(float_to_integer(1.0))

# # Purpose: checks if a float is positive
# # Example:
# #   Call:    float_is_positive(1.0)
# #   Returns: True
# #   Call:    float_is_positive(-1.0)
# #   Returns: False
# def float_is_positive(float):
#     if float > 0:
#         return True
#     return False

# print(float_is_positive(1.0))
# print(float_is_positive(-1.0))


# # Purpose: checks if a float is negative
# # Example:
# #   Call:    float_is_negative(1.0)
# #   Returns: False
# #   Call:    float_is_negative(-1.0)
# #   Returns: True
# def float_is_negative(float):
#     if float < 0:
#         return True
#     return False

# print(float_is_negative(1.0))
# print(float_is_negative(-1.0))


# # Purpose: converts a boolean to a string
# # Example:
# #   Call:    boolean_to_string(True)
# #   Returns: "True"
# def boolean_to_string(boolean):
#     return str(boolean)
    
# print(boolean_to_string(True))


# Purpose: checks if a string starts with the letter a
# Example:
#   Call:    starts_with_the_letter_a("apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Rock")
#   Returns: False
# def starts_with_the_letter_a(string):
#     if string[0] == "a" or string[0] == "A":
#         return True
#     return False

# print("\n")
# print(starts_with_the_letter_a("apple"))
# print(starts_with_the_letter_a("Apple"))
# print(starts_with_the_letter_a("Rock"))


# # Purpose: checks if a string ends with the letter a
# # Example:
# #   Call:    ends_with_the_letter_a("Java")
# #   Returns: True
# #   Call:    ends_with_the_letter_a("JAVA")
# #   Returns: True
# #   Call:    ends_with_the_letter_a("Python")
# #   Returns: False
# def ends_with_the_letter_a(string):
#     if string[-1] == "a" or string[-1] == "A":
#         return True
#     return False

# print(ends_with_the_letter_a("Java"))
# print(ends_with_the_letter_a("JAVA"))
# print(ends_with_the_letter_a("Python"))

# # Purpose: checks if a string contains the word hello
# # Example:
# #   Call:    contains_hello("hello world")
# #   Returns: True
# #   Call:    contains_hello("HELLO WORLD")
# #   Returns: True
# #   Call:    contains_hello("world")
# #   Returns: False
# def contains_hello(string):
#     if "hello" in string or "HELLO" in string:
#         return True
#     return False

# print(contains_hello("hello world"))
# print(contains_hello("HELLO WORLD"))
# print(contains_hello("world"))

# # Purpose: replaces the word hello with the word goodbye
# # Note: you don't need to match 'Hello' or 'HELLO' here,
# #       lowercase only is the aim.
# # Example:
# #   Call:    substitute_hello_with_goodbye("hello folks")
# #   Returns: "goodbye folks"
# #   Call:    substitute_hello_with_goodbye("Hello folks")
# #   Returns: "Hello folks"
# def substitute_hello_with_goodbye(string):
#     if "hello" in string:
#         return "goodbye folks"
#     return string
        

# print(substitute_hello_with_goodbye("hello folks"))
# print(substitute_hello_with_goodbye("Hello folks"))

# # Purpose: removes the letter x from a string
# # Example:
# #   Call:    remove_x("xoxo")
# #   Returns: "oo"
# #   Call:    remove_x("OXO")
# #   Returns: "OO"
# def remove_x(string):
#     return string.replace("x", "").replace("X", "")


# print(remove_x("xoxo"))
# print(remove_x("OXO"))

# # Purpose: returns the first half of a string
# # Example:
# #   Call:    first_half("coding")
# #   Returns: "cod"
# # Note: you can assume the string will always have an even number of characters
# def first_half(string):
#     total = len(string)
#     half_length = total // 2
#     return string[:half_length]

# print(first_half("coding"))

# # Purpose: returns the second half of a string
# # Example:
# #   Call:    second_half("coding")
# #   Returns: "ing"
# # Note: you can assume the string will always have an even number of characters
# def second_half(string):
#     total = len(string)
#     half_length = total // 2
#     return string[half_length:]

# print(second_half("coding"))


# Purpose: implements a childhood game
# Rules:   if the number is divisible by 3, return 'fizz'
#          if the number is divisible by 5, return 'buzz'
#          if the number is divisible by 15, return 'fizzbuzz'
#          otherwise, return the number
# Clue: you can check divisibility using modulo (%)
# Example:
#   Call:    fizz_buzz(3)
#   Returns: "fizz"
#   Call:    fizz_buzz(5)
#   Returns: "buzz"
#   Call:    fizz_buzz(15)
#   Returns: "fizzbuzz"
#   Call:    fizz_buzz(8)
#   Returns: 8
# def fizz_buzz(number):
#     if number % 15 == 0:
#         return "fizzbuzz"
#     if number % 3 == 0:
#         return "fizz"
#     if number % 5 == 0:
#         return "buzz"
#     else:
#         return number

# print(fizz_buzz(3))
# print(fizz_buzz(5))
# print(fizz_buzz(15))
# print(fizz_buzz(8))

# # Purpose: responds to the user's greeting
# # Rules:   if the greeting is 'good morning'
# #          return 'good morning to you too'
# #          if the greeting is 'hello'
# #          return 'hi'
# #          if the greeting is anything else
# #          return the greeting that was received
# # Example:
# #   Call:    reply_to("good morning")
# #   Returns: "good morning to you too"
# #   Call:    reply_to("hello")
# #   Returns: "hi"
# #   Call:    reply_to("how are you?")
# #   Returns: "how are you?"
# def reply_to(greeting):
#     if greeting == "good morning":
#         return "good morning to you too"
#     if greeting == "hello":
#         return "hi"
#     else:
#         return greeting 

# print(reply_to("good morning"))
# print(reply_to("hello"))
# print(reply_to("how are you?"))

# # Purpose: deducts 10 from a number if it is greater than or equal to 10,
# #          otherwise returns the number
# # Example:
# #   Call:    deduct_10_if_possible(25)
# #   Returns: 15
# #   Call:    deduct_10_if_possible(10)
# #   Returns: 0
# #   Call:    deduct_10_if_possible(9)
# #   Returns: 9
# def deduct_10_if_possible(number):
#     if number >= 10:
#         number = number - 10
#         return number
#     return number

# print(deduct_10_if_possible(25))
# print(deduct_10_if_possible(10))
# print(deduct_10_if_possible(9))


# # Purpose: if the number is below 100, return 100, otherwise return the number
# # Example:
# #   Call:    top_up_to_100(25)
# #   Returns: 100
# #   Call:    top_up_to_100(100)
# #   Returns: 100
# #   Call:    top_up_to_100(125)
# #   Returns: 125
# def top_up_to_100(number):
#     if number < 100:
#         return 100
#     return number
    
# print(top_up_to_100(25))
# print(top_up_to_100(100))
# print(top_up_to_100(125))




# Method name: say_hello
# Purpose: returns the string 'hello'
# Arguments: none
# Example:
#   Call:    say_hello()
#   Returns: "hello"

# def say_hello():
#     return "hello"

# print(say_hello())



# # Method name: say_goodbye
# # Purpose: returns the string 'goodbye'
# # Arguments: none
# # Example:
# #   Call:    say_goodbye()
# #   Returns: "goodbye"

# def say_goodbye():
#     return "goodbye"

# print(say_goodbye())

# # Method name: say_hello_to
# # Purpose: greets the given name
# # Arguments: one string
# # Example:
# #   Call:    say_hello_to("Sam")
# #   Returns: "Hello, Sam!"

# def say_hello_to(name):
#     return f"Hello, {name}!"

# print(say_hello_to("Sam"))


# # Method name: say_goodbye_to
# # Purpose: says goodbye to the given name
# # Arguments: one string
# # Example:
# #   Call:    say_goodbye_to("Sam")
# #   Returns: "Goodbye, Sam!"
# def say_goodbye_to(name):
#     return f"Goodbye, {name}!"

# print(say_goodbye_to("Sam"))



# # Method name: square
# # Purpose: multiplies the given number by itself
# # Arguments: one number
# # Example:
# #   Call:    square(5)
# #   Returns: 25

# def square(number):
#     return number * number

# print(square(5))



# # Method name: divisible_by_three
# # Purpose: returns true if the given number is divisible by three
# # Arguments: one number
# # Example:
# #   Call:    divisible_by_three(9)
# #   Returns: True
# #   Call:    divisible_by_three(10)
# #   Returns: False

# def divisible_by_three(number):
#     if number % 3 == 0:
#         return True
#     return False


# print(divisible_by_three(9))
# print(divisible_by_three(10))


# # Method name: add
# # Purpose: adds two numbers together
# # Arguments: two numbers
# # Example:
# #   Call:    add(5, 10)
# #   Returns: 15

# def add(x, y):
#     return x + y

# print(add(5, 10))



# # Method name: multiply
# # Purpose: multiplies two numbers together
# # Arguments: two numbers
# # Example:
# #   Call:    multiply(5, 10)
# #   Returns: 50
# def multiply(x, y):
#     return x * y


# print(multiply(5, 10))


# # Method name: add_number_strings
# # Purpose: adds two numbers given as strings
# # Arguments: two strings
# # Example:
# #   Call:    add_number_strings("5", "10")
# #   Returns: 15
# # Note: return value should be a number, not a string

# def add_number_strings(x, y):
#     return int(x) + int(y)

# print(add_number_strings("5", "10"))


# # Method name: multiply_number_strings
# # Purpose: multiplies two numbers given as strings
# # Arguments: two strings
# # Example:
# #   Call:    multiply_number_strings("5", "10")
# #   Returns: 50
# # Note: return value should be a number, not a string

# def multiply_number_strings(x, y):
#     return int(x) * int(y)

# print(multiply_number_strings("5", "10"))




# # Method name: both_odd
# # Purpose: returns true if both numbers are odd
# # Arguments: two numbers
# # Example:
# #   Call:    both_odd(5, 11)
# #   Returns: True
# #   Call:    both_odd(5, 10)
# #   Returns: False
# #   Call:    both_odd(6, 10)
# #   Returns: False

# def both_odd(x, y):
#     if x % 2 == 1 and y % 2 == 1:
#         return True
#     return False


# print(both_odd(5, 11))
# print(both_odd(5, 10))
# print(both_odd(6, 10))


# # Method name: both_even
# # Purpose: returns true if both numbers are even
# # Arguments: two numbers
# # Example:
# #   Call:    both_even(4, 10)
# #   Returns: True
# #   Call:    both_even(5, 10)
# #   Returns: False
# #   Call:    both_even(5, 11)
# #   Returns: False

# def both_even(x, y):
#     if x % 2 == 0 and y % 2 == 0:
#         return True
#     return False

# print(both_even(4, 10))
# print(both_even(5, 10))
# print(both_even(5, 11))



# # Method name: one_odd
# # Purpose: returns true if at least one number is odd
# # Arguments: two numbers
# # Example:
# #   Call:    one_odd(5, 10)
# #   Returns: True
# #   Call:    one_odd(5, 11)
# #   Returns: True
# #   Call:    one_odd(4, 8)
# #   Returns: False

# def one_odd(x, y):
#     return x % 2 == 1 or y % 2 == 1
     

# print(one_odd(5, 10))
# print(one_odd(5, 11))
# print(one_odd(4, 8))


# # Method name: one_even
# # Purpose: returns true if at least one number is even
# # Arguments: two numbers
# # Example:
# #   Call:    one_even(5, 10)
# #   Returns: True
# #   Call:    one_even(4, 10)
# #   Returns: True
# #   Call:    one_even(5, 9)
# #   Returns: False

# def one_even(x, y):
#     return x % 2 == 0 or y % 2 == 0

# print(one_even(5, 10))
# print(one_even(4, 10))
# print(one_even(5, 9))

# # Method name: truncate_string
# # Purpose: truncates (shortens) a string to 10 characters
# # Arguments: one string
# # Rules:
# #   If the string is longer than 10 characters
# #   return the first 10 characters followed by '...'
# #   If the string is 10 characters or less
# #   return the whole string
# # Example:
# #   Call:    truncate_string("This is a long string")
# #   Returns: "This is a ..."
# #   Call:    truncate_string("Short")
# #   Returns: "Short"

# def truncate_string(string):
#     if len(string) > 10:
#         return string[:10] 
#     if len(string) <= 10:
#         return string

# print(truncate_string("This is a long string"))
# print(truncate_string("Short"))



# Method name: first_element
# Purpose: returns the first element of the given list
# Arguments: one list
# Example:
#   Call:    first_element([1, 2, 3])
#   Returns: 1

# def first_element(lst):
#     return lst[0]

# print(first_element([1, 2, 3]))


# # Method name: second_element
# # Purpose: returns the second element of the given list
# # Arguments: one list
# # Example:
# #   Call:    second_element([1, 2, 3])
# #   Returns: 2

# def second_element(lst):
#     return lst[1]

# print(second_element([1, 2, 3]))

# # Method name: last_element
# # Purpose: returns the last element of the given list
# # Arguments: one list
# # Example:
# #   Call:    last_element([1, 2, 3])
# #   Returns: 3

# def last_element(lst):
#     return lst[-1]

# print(last_element([1, 2, 3]))


# # Method name: first_two_elements
# # Purpose: returns the first two elements of the given list
# # Arguments: one list
# # Example:
# #   Call:    first_two_elements([1, 2, 3])
# #   Returns: [1, 2]

# def first_two_elements(lst):
#     return lst[:2]

# print(first_two_elements([1, 2, 3]))



# # Method name: first_three_elements
# # Purpose: returns the first three elements of the given list
# # Arguments: one list
# # Example:
# #   Call:    first_three_elements([1, 2, 3, 4])
# #   Returns: [1, 2, 3]

# def first_three_elements(lst):
#     return lst[:3]

# print(first_three_elements([1, 2, 3, 4]))


# # Method name: total
# # Purpose: returns the sum of all the elements in the given list
# # Arguments: one list
# # Example:
# #   Call:    total([1, 2, 3])
# #   Returns: 6

# def total(lst):
#     sum_total = 0 
#     for i in lst:
#         sum_total += i
#     return sum_total

# print(total([1, 2, 3]))



# # Method name: lowest_number
# # Purpose: returns the lowest number in the given list
# # Arguments: one list
# # Example:
# #   Call:    lowest_number([4, 2, 6])
# #   Returns: 2

# def lowest_number(lst):
#     lst = sorted(lst)
#     return lst[0]

# print(lowest_number([4, 2, 6]))


# # Method name: highest_number
# # Purpose: returns the highest number in the given list
# # Arguments: one list
# # Example:
# #   Call:    highest_number([4, 6, 2])
# #   Returns: 6

# def highest_number(lst):
#     lst = sorted(lst)[::-1]
#     return lst[0]

# print(highest_number([4, 6, 2]))

# # Method name: the_beatles
# # Purpose: returns the list ['john', 'paul', 'george', 'ringo']
# # Arguments: none
# # Example:
# #   Call:    the_beatles()
# #   Returns: ['john', 'paul', 'george', 'ringo']

# def the_beatles(lst):
#     return lst
# print(the_beatles(['john', 'paul', 'george', 'ringo']))


# # Method name: i_joined_the_beatles
# # Purpose: adds the given name to the list ['john', 'paul', 'george', 'ringo']
# # Arguments: one string
# # Example:
# #   Call:    i_joined_the_beatles('yoko')
# #   Returns: ['john', 'paul', 'george', 'ringo', 'yoko']

# def i_joined_the_beatles(string):
#     beatles = ['john', 'paul', 'george', 'ringo']
#     beatles.append(string)
#     return beatles

# print(i_joined_the_beatles('yoko'))

# # Method name: we_joined_the_beatles
# # Purpose: adds the given names to the list ['john', 'paul', 'george', 'ringo']
# # Arguments: one list
# # Example:
# #   Call:    we_joined_the_beatles(['yoko', 'stuart'])
# #   Returns: ['john', 'paul', 'george', 'ringo', 'yoko', 'stuart']

# def we_joined_the_beatles(lst):
#     beatles = ['john', 'paul', 'george', 'ringo']
#     beatles.extend(lst)
#     return beatles

# print(we_joined_the_beatles(['yoko', 'stuart']))

# # Method name: remove_nones_from_list
# # Purpose: removes all the None values from the given list
# # Arguments: one list
# # Example:
# #   Call:    remove_nones_from_list([1, None, 2, None, 3])
# #   Returns: [1, 2, 3]

# def remove_nones_from_list(lst):
#     return [item for item in lst if item is not None]

# print(remove_nones_from_list([1, None, 2, None, 3]))


# # Method name: double_list
# # Purpose: returns a list with all the elements of the given list repeated twice
# # Arguments: one list
# # Example:
# #   Call:    double_list([1, 2, 3])
# #   Returns: [1, 2, 3, 1, 2, 3]

# def double_list(lst):
#     return [item for item in lst * 2]

# print(double_list([1, 2, 3]))

# # Method name: unique_elements
# # Purpose: returns a list with all the unique elements of the given list
# # Arguments: one list
# # Example:
# #   Call:    unique_elements([1, 2, 1, 3, 2, 3])
# #   Returns: [1, 2, 3]

# def unique_elements(lst):
#     seen = set()
#     unique = []
#     for item in lst:
#         if item not in seen:
#             unique.append(item)
#             seen.add(item)
#     return unique

# print(unique_elements([1, 2, 1, 3, 2, 3]))  # returns [1, 2, 3]


# # Method name: add_to_list
# # Purpose: adds the given element to the given list
# # Arguments: one list and one element
# # Example:
# #   Call:    add_to_list(["a", "b", "c"], "d")
# #   Returns: ["a", "b", "c", "d"]

# def add_to_list(lst, element):
#     lst.append(element)
#     return lst

# print(add_to_list(["a", "b", "c"], "d"))

# == DICTIONARY EXERCISES ==
dsdf
# Method name: new_band_member
# Purpose: merges a given dictionary into an existing dictionary
# Arguments: one dictionary
# Note: {"vocalist": "miss piggy", "lead_guitar": "scooter"}
# Example:
#   Call:    new_band_member({"bass": "flea"})
#   Returns: {"vocalist": "miss piggy", "lead_guitar": "scooter", "bass": "flea"}



# Method name: all_values
# Purpose: returns a list of all the values in the given dictionary
# Arguments: one dictionary
# Example:
#   Call:    all_values({"a": 1, "b": 2, "c": 3})
#   Returns: [1, 2, 3]



# Method name: all_keys
# Purpose: returns a list of all the keys in the given dictionary
# Arguments: one dictionary
# Example:
#   Call:    all_keys({"a": 1, "b": 2, "c": 3})
#   Returns: ["a", "b", "c"]



# Method name: remove_nones_from_dictionary
# Purpose: removes all pairs from a given dictionary where the value is None
# Arguments: one dictionary
# Example:
#   Call:    remove_nones_from_dictionary({"a": 1, "b": None, "c": 3})
#   Returns: {"a": 1, "c": 3}




# Method name: touch_in
# Purpose: creates a dictionary from a given tube station and time
# Arguments: two strings, one for the tube station and one for the time
# Example:
#   Call:    touch_in('Aldgate East', '2022/01/30 17:12')
#   Returns: {'entrypoint': 'Aldgate East', 'time': '2022/01/30 17:12'}


import datetime

# == INSTRUCTIONS ==
#
# In these exercises you will build small classes.
#
# Some will have no methods. Some will have one or two simple methods. Some will
# have more complex methods.
#
# Here is an example of some exercise instructions and a solution.
#
# Class name: Greeter
# Purpose: say hello and goodbye to a user with a given name
# Methods:
#   1. Name: __init__
#      Arguments: one, a string representing a name
#   2. Name: say_hello
#      Arguments: none
#      Returns: a string like 'Hello, NAME!'
#   3. Name: say_goodbye
#      Arguments: none
#      Returns: a string like 'Goodbye, NAME!'
# Example usage:
#   > greeter = Greeter('Bobby')
#   > greeter.say_hello()
#   'Hello, Bobby!'
#   > greeter.say_goodbye()
#   'Goodbye, Bobby!'
#
# Example solution follows.

class Greeter():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return 'Hello, ' + self.name + "!"

    def say_goodbye(self):
        return 'Goodbye, ' + self.name + "!"


# == EXERCISES ==

# Class name: Animal
# Purpose: a generic animal
# Methods:
#   1. Name: __init__
#      Arguments: none
#   No other methods required
# Example usage:
#   > animal = Animal()
#   > animal
#   <Animal object at 0x7f8b8c0b8e80>



# Class name: Vehicle
# Purpose: a generic vehicle
# Methods:
#   1. Name: __init__
#      Arguments: none
#   No other methods required
# Example usage:
#   > vehicle = Vehicle()
#   > vehicle
#   <Vehicle object at 0x7f8b8c0b8e80>



# Class name: Cat
# Purpose: miaows at the user
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: speak
#      Arguments: none
#      Returns: the string 'miaow'
# Example usage:
#   > cat = Cat()
#   > cat.speak()
#   'miaow'



# Class name: Dog
# Purpose: woofs at the user
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: speak
#      Arguments: none
#      Returns: the string 'woof'
# Example usage:
#   > dog = Dog()
#   > dog.speak()
#   'woof'



# Class name: StringFormatter
# Purpose: transforms strings
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: block_caps
#      Arguments: one, a string
#      Returns: the string in block caps
#   3. Name: lower_case
#      Arguments: one, a string
#      Returns: the string in lower case
# Example usage:
#   > string_formatter = StringFormatter()
#   > string_formatter.block_caps('hello')
#   'HELLO'
#   > string_formatter.lower_case('HELLO')
#   'hello'



# Class name: Calculator
# Purpose: performs basic arithmetic
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Arguments: two numbers
#      Returns: the result of adding the two numbers
#   3. Name: multiply
#      Arguments: two numbers
#      Returns: the result of multiplying the first by the second
#   4. Name: subtract
#      Arguments: two numbers
#      Returns: the result of subtracting the second from the first
#   5. Name: divide
#      Arguments: two numbers
#      Returns: the result of dividing the first by the second
# Example usage:
#   > calculator = Calculator()
#   > calculator.add(1, 2)
#   3
#   > calculator.multiply(2, 3)
#   6
#   > calculator.subtract(3, 2)
#   1
#   > calculator.divide(6, 2)
#   3.0



# Class name: Apprentice
# Purpose: represents an apprentice
# Fields:
#   1. Name: name
#      Type: string
#      Purpose: the apprentice's name
#   2. Name: cohort
#      Type: string
#      Purpose: the cohort the apprentice is in
# Methods:
#   1. Name: __init__
#      Arguments: one string representing a name, one string representing a cohort
#   2. Name: format_details
#      Arguments: none
#      Returns: the name and cohort, separated by one comma and one space
# Example usage:
#   > apprentice = Apprentice('Rita Smith', 'June 2030')
#   > apprentice.name
#   'Rita Smith'
#   > apprentice.cohort
#   'June 2030'
#   > apprentice.format_details()
#   'Rita Smith, June 2030'



# Class name: Cohort
# Purpose: represents a cohort
# Fields:
#   1. Name: name
#      Type: string
#      Purpose: the cohort name
#   2. Name: start_date
#      Type: Date
#      Purpose: the cohort start date
#   3. Name: end_date
#      Type: Date
#      Purpose: the cohort end date
# Methods:
#   1. Name: __init__
#      Arguments: one string representing a name,
#                 one string representing a start_date,
#                 one string representing an end_date
#   2. Name: calculate_duration
#      Arguments: none
#      Returns: the number of days between start_date and end_date
# Example usage:
#   > cohort = Cohort('June 2020', '2020-06-01', '2020-09-01')
#   > cohort.name
#   'June 2020'
#   > cohort.start_date
#   datetime.date(2020, 6, 1)
#   > cohort.end_date
#   datetime.date(2020, 9, 1)
#   > cohort.calculate_duration()
#   92


# == INSTRUCTIONS ==
#
# In these exercises you will recap basic dictionary and list operations, then
# go deeper on both topics.
#
# The requirements will always start with the name of the function. Use this
# name exactly or the tests won't be able to find it.
#
# Then there will be a description of what the function should do. Note that
# some solutions will require more than one line of code.
#
# You won't find everything that you need in our materials. Use the Python Docs
# and Google liberally if you get stuck.

# == LIST EXERCISES ==

# Method name: fourth_element
# Purpose: returns the fourth element of the given list
# Arguments: one list
# Example:
#   Call:    fourth_element([1, 2, 3, 4, 5])
#   Returns: 4



# Method name: average
# Purpose: returns the average (the mean) of the given list
# Arguments: one list
# Example:
#   Call:    average([3, 1, 44, 1])
#   Returns: 12.25



# Method name: lowest_squared
# Purpose: returns the lowest number squared
# Arguments: one list
# Example:
#   Call:    lowest_squared([5, 3, 44, 7])
#   Returns: 9



# Method name: highest_squared
# Purpose: returns the highest number squared
# Arguments: one list
# Example:
#   Call:    highest_squared([5, 3, 44, 7])
#   Returns: 1936



# Method name: starts_with_a
# Purpose: returns only elements starting with 'a'
# Arguments: one list
# Example:
#   Call:    starts_with_a(['banana', 'apple', 'orange', 'avocado'])
#   Returns: ['apple', 'avocado']



# Method name: starts_with_a_vowel
# Purpose: returns only the elements that start with a vowel
# Arguments: one list
# Example:
#   Call:    starts_with_a_vowel(['banana', 'apple', 'orange', 'avocado'])
#   Returns: ['apple', 'orange', 'avocado']



# Method name: reverse_each_element
# Purpose: reverses each string in the given list
# Arguments: one list
# Example:
#   Call:    reverse_each_element(['one', 'two'])
#   Returns: ['eno', 'owt']



# Method name: sort_by_last_letter
# Purpose: returns the list, sorted by the last letter alphabetically
# Arguments: one list
# Example:
#   Call:    sort_by_last_letter(['banana', 'apple', 'carrot', 'avocado'])
#   Returns: ['banana', 'apple', 'avocado', 'carrot']



# Method name: greater_than_5
# Purpose: returns only numbers greater than 5
# Arguments: one list
# Example:
#   Call:    greater_than_5([9, 3, 44, 7])
#   Returns: [9, 44, 7]



# Method name: greater_than
# Purpose: returns only the elements that are greater than the number provided
# Arguments: one list and one number
# Example:
#   Call:    greater_than([9, 3, 6, 44, 7, 7], 6)
#   Returns: [9, 44, 7, 7]



# Method name: less_than
# Purpose: returns only the elements that are less than the number provided
# Arguments: one list and one number
# Example:
#   Call:    less_than([9, 3, 6, 44, 1, 7, 7], 6)
#   Returns: [3, 1]



# Method name: words_shorter_than
# Purpose: returns only the elements that have fewer characters than the number provided
# Arguments: one list and one number
# Example:
#   Call:    words_shorter_than(['banana', 'apple', 'orange', 'nut', 'avocado'], 6)
#   Returns: ['apple', 'nut']



# Method name: all_above
# Purpose: returns True if all elements are greater than the number provided
# Arguments: one list and one number
# Example:
#   Call:    all_above([9, 3, 6, 44, 1, 7, 7], 6)
#   Returns: False
#   Call:    all_above([9, 3, 6, 44, 1, 7, 7], 0)
#   Returns: True



# Method name: all_below
# Purpose: returns True if all elements are less than the number provided
# Arguments: one list and one number
# Example:
#   Call:    all_below([9, 3, 6, 44, 1, 7, 7], 6)
#   Returns: False
#   Call:    all_below([9, 3, 6, 44, 1, 7, 7], 100)
#   Returns: True



# Method name: multiply_each_by
# Purpose: returns a new list with each element multiplied by the number provided
# Arguments: one list and one number
# Example:
#   Call:    multiply_each_by([9, 3, 6, 44, 1, 7, 7], 2)
#   Returns: [18, 6, 12, 88, 2, 14, 14]



# == DICTIONARY EXERCISES ==

# Method name: values_summed
# Purpose: returns the total of all the values in the given dictionary
# Arguments: one dictionary
# Example:
#   Call:    values_summed({'cat': 4, 'person': 2, 'centipede': 100})
#   Returns: 106



# Method name: add_key_value_pair
# Purpose: returns the dictionary with the new key and value added
# Arguments: one dictionary, one key and one value
# Example:
#   Call:    add_key_value_pair({'cat': 4, 'person': 2, 'centipede': 100}, 'dog', 4)
#   Returns: {'cat': 4, 'person': 2, 'centipede': 100, 'dog': 4}



# Method name: remove_key_value_pair
# Purpose: returns the dictionary with the key and value removed
# Arguments: one dictionary and one key
# Example:
#   Call:    remove_key_value_pair({'cat': 4, 'person': 2, 'centipede': 100}, 'cat')
#   Returns: {'person': 2, 'centipede': 100}



# Method name: where_value_below
# Purpose: returns key value pairs where the value is less than the number provided
# Arguments: one dictionary and one number
# Example:
#   Call:    where_value_below({'cat': 4, 'person': 2, 'centipede': 100}, 5)
#   Returns: {'cat': 4, 'person': 2}



# Method name: where_key_starts_with
# Purpose: returns key value pairs where the key starts with the letter provided
# Arguments: one dictionary and one letter
# Example:
#   Call:    where_key_starts_with({'cat': 4, 'person': 2, 'centipede': 100}, 'c')
#   Returns: {'cat': 4, 'centipede': 100}

# == INSTRUCTIONS ==
#
# In these exercises you will build small classes.
#
# The first ones will be familiar, do them without looking at your previous
# work. The later ones will be more complex.
#
# Here is an example of some exercise instructions and a solution.
#
# Class name: ExampleGreeter
# Purpose: say hello and goodbye to a user with a given name
# Methods:
#   1. Name: __init__
#      Arguments: one, a string representing a name
#   2. Name: say_hello
#      Arguments: none
#      Returns: a string like 'Hello, NAME!'
#   3. Name: say_goodbye
#      Arguments: none
#      Returns: a string like 'Goodbye, NAME!'
# Example usage:
#   > greeter = ExampleGreeter('Bobby')
#   > greeter.say_hello()
#   'Hello, Bobby!'
#   > greeter.say_goodbye()
#   'Goodbye, Bobby!'
#
# Example solution:
# class ExampleGreeter():
#     def __init__(self, name):
#         self.name = name
#     def say_hello(self):
#         return 'Hello, ' + self.name + '!'
#     def say_goodbye(self):
#         return 'Goodbye, ' + self.name + '!'



# == EXERCISES ==

# Class name: Greeter
# Purpose: say various greetings to a user with a given name
# Methods:
#   1. Name: hello
#      Arguments: one, a string representing a name
#      Returns: a string like 'Hello, NAME!'
#   2. Name: goodbye
#      Arguments: one, a string representing a name
#      Returns: a string like 'Goodbye, NAME!'
#   3. Name: good_night
#      Arguments: one, a string representing a name
#      Returns: a string like 'Good night, NAME!'
#   4. Name: good_morning
#      Arguments: one, a string representing a name
#      Returns: a string like 'Good morning, NAME!'
# Example usage:
#   > greeter = Greeter()
#   > greeter.hello('Bobby')
#   'Hello, Bobby!'
#   > greeter.goodbye('Bobby')
#   'Goodbye, Bobby!'
#   > greeter.good_night('Bobby')
#   'Good night, Bobby!'
#   > greeter.good_morning('Bobby')
#   'Good morning, Bobby!'



# Class name: Basket
# Purpose: store a list of items
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Arguments: one item of any type
#      Returns: nothing
#   3. Name: list_items
#      Arguments: none
#      Returns: a list of all the items that have been added
# Example usage:
#   > basket = Basket()
#   > basket.add('apple')
#   > basket.add('banana')
#   > basket.add('orange')
#   > basket.list_items()
#   ['apple', 'banana', 'orange']



# Class name: Calculator
# Purpose: perform simple calculations and track the history
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Arguments: two numbers
#      Returns: the result of adding the two numbers
#   3. Name: multiply
#      Arguments: two numbers
#      Returns: the result of multiplying the first by the second
#   4. Name: subtract
#      Arguments: two numbers
#      Returns: the result of subtracting the second from the first
#   5. Name: divide
#      Arguments: two numbers
#      Returns: the result of dividing the first by the second
#   6. Name: list_history
#      Arguments: none
#      Returns: a list of all the previous results calculations
# Example usage:
#   > calculator = Calculator()
#   > calculator.add(1, 2)
#   3
#   > calculator.multiply(3, 4)
#   12
#   > calculator.subtract(5, 6)
#   -1
#   > calculator.divide(7, 8)
#   0.875
#   > calculator.list_history()
#   [3, 12, -1, 0.875]



# Class name: Cohort
# Purpose: store a list of students
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add_student
#      Arguments: one dictionary representing a student
#      Returns: nothing
#   3. Name: list_students
#      Arguments: none
#      Returns: a list of all the students that have been added
#   4. Name: list_employed_by
#      Arguments: one string, the name of an employer
#      Returns: a list of all the students who work for that employer
# Example usage:
#   > cohort = Cohort()
#   > cohort.add_student({'name' : 'Jo', 'employer' : 'NASA'})
#   > cohort.add_student({'name' : 'Alex', 'employer' : 'NASA'})
#   > cohort.add_student({'name' : 'Bobby', 'employer' : 'Google'})
#   > cohort.list_students()
#   [{'name' : 'Jo', 'employer' : 'NASA'}, {'name' : 'Alex', 'employer' : 'NASA'}, {'name' : 'Bobby', 'employer' : 'Google'}]
#   > cohort.list_employed_by('NASA')
#   [{'name' : 'Jo', 'employer' : 'NASA'}, {'name' : 'Alex', 'employer' : 'NASA'}]



# Class name: Person
# Purpose: store a person's name, pets and addresses
# Methods:
#   1. Name: __init__
#      Arguments: one complex dictionary, see below for structure.
#   2. Name: get_work_address
#      Arguments: none
#      Returns: the work address in a nice format
#   3. Name: get_home_address
#      Arguments: none
#      Returns: the home address in a nice format
#   4. Name: get_pets
#      Arguments: none
#      Returns: a nice summary of the person's pets
# Example usage:
#   > person = Person({
#       'name' : 'Alex',
#       'pets' : [
#         {'name' : 'Arthur', 'animal' : 'cat'},
#         {'name' : 'Judith', 'animal' : 'dog'},
#         {'name' : 'Gwen', 'animal' : 'goldfish'}
#       ],
#       'addresses' : [
#         {'name' : 'work', 'building' : '50', 'street' : 'Commercial Street'},
#         {'name' : 'home', 'building' : '10', 'street' : 'South Street'}
#       ]
#     })
#   > person.get_work_address()
#   '50 Commercial Street'
#   > person.get_home_address()
#   '10 South Street'
#   > person.get_pets()
#   'Alex has 3 pets: a cat called Arthur, a dog called Judith, a goldfish called Gwen'

