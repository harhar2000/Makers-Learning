# == EXERCISES ==

# Method name: say_hello
# Purpose: returns the string 'hello'
# Arguments: none
# Example:
#   Call:    say_hello()
#   Returns: "hello"

def say_hello():
    return "hello"

print(say_hello())


# Method name: say_goodbye
# Purpose: returns the string 'goodbye'
# Arguments: none
# Example:
#   Call:    say_goodbye()
#   Returns: "goodbye"

def say_goodbye():
    return "goodbye"

print(say_goodbye())


# Method name: say_hello_to
# Purpose: greets the given name
# Arguments: one string
# Example:
#   Call:    say_hello_to("Sam")
#   Returns: "Hello, Sam!"

def say_hello_to(string):
    return f"Hello, {string}!"

print(say_hello_to("Sam"))


# Method name: say_goodbye_to
# Purpose: says goodbye to the given name
# Arguments: one string
# Example:
#   Call:    say_goodbye_to("Sam")
#   Returns: "Goodbye, Sam!"

def say_goodbye_to(string):
    return f"Goodbye, {string}!"

print(say_goodbye_to("Sam"))


# Method name: square
# Purpose: multiplies the given number by itself
# Arguments: one number
# Example:
#   Call:    square(5)
#   Returns: 25

def squared(number):
    total = number * number
    return total

print(squared(5))


# Method name: divisible_by_three
# Purpose: returns true if the given number is divisible by three
# Arguments: one number
# Example:
#   Call:    divisible_by_three(9)
#   Returns: True
#   Call:    divisible_by_three(10)
#   Returns: False

def divide_three(number):
    return number % 3 == 0

print(divide_three(9))
print(divide_three(10))


# Method name: add
# Purpose: adds two numbers together
# Arguments: two numbers
# Example:
#   Call:    add(5, 10)
#   Returns: 15

def add(x, y):
    total = x + y
    return total

print(add(5, 10))


# Method name: multiply
# Purpose: multiplies two numbers together
# Arguments: two numbers
# Example:
#   Call:    multiply(5, 10)
#   Returns: 50

def multiply(x, y):
    total = x * y
    return total

print(multiply(5, 10))


# Method name: add_number_strings
# Purpose: adds two numbers given as strings
# Arguments: two strings
# Example:
#   Call:    add_number_strings("5", "10")
#   Returns: 15
# Note: return value should be a number, not a string

def add_number_strings(x, y):
    x = int(x)
    y = int(y)
    total = x + y
    return total

print(add_number_strings("5", "10"))


# Method name: multiply_number_strings
# Purpose: multiplies two numbers given as strings
# Arguments: two strings
# Example:
#   Call:    multiply_number_strings("5", "10")
#   Returns: 50
# Note: return value should be a number, not a string

def multiply_number_strings(x, y):
    x = int(x)
    y = int(y)
    total = x * y
    return total

print(multiply_number_strings("5", "10"))


# Method name: both_odd
# Purpose: returns true if both numbers are odd
# Arguments: two numbers
# Example:
#   Call:    both_odd(5, 11)
#   Returns: True
#   Call:    both_odd(5, 10)
#   Returns: False
#   Call:    both_odd(6, 10)
#   Returns: False

def both_odd(x, y):
    if x % 2 == 1 and y % 2 == 1:
        return True
    return False


print(both_odd(5, 11))
print(both_odd(5, 10))
print(both_odd(6, 10))


# Method name: both_even
# Purpose: returns true if both numbers are even
# Arguments: two numbers
# Example:
#   Call:    both_even(4, 10)
#   Returns: True
#   Call:    both_even(5, 10)
#   Returns: False
#   Call:    both_even(5, 11)
#   Returns: False

def both_even(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return True
    return False

print(both_even(4, 10))
print(both_even(5, 10))
print(both_even(5, 11))


# Method name: one_odd
# Purpose: returns true if at least one number is odd
# Arguments: two numbers
# Example:
#   Call:    one_odd(5, 10)
#   Returns: True
#   Call:    one_odd(5, 11)
#   Returns: True
#   Call:    one_odd(4, 8)
#   Returns: False

def one_odd(x, y):
    if x % 2 == 1 or y % 2 == 1:
        return True
    return False

print(one_odd(5, 10))
print(one_odd(5, 11))
print(one_odd(4, 8))


# Method name: one_even
# Purpose: returns true if at least one number is even
# Arguments: two numbers
# Example:
#   Call:    one_even(5, 10)
#   Returns: True
#   Call:    one_even(4, 10)
#   Returns: True
#   Call:    one_even(5, 9)
#   Returns: False

def one_even(x, y):
    if x % 2 == 0 or y % 2 == 0:
        return True
    return False

print(one_even(5, 10))
print(one_even(4, 10))
print(one_even(5, 9))


# Method name: truncate_string
# Purpose: truncates (shortens) a string to 10 characters
# Arguments: one string
# Rules:
#   If the string is longer than 10 characters
#   return the first 10 characters followed by '...'
#   If the string is 10 characters or less
#   return the whole string
# Example:
#   Call:    truncate_string("This is a long string")
#   Returns: "This is a ..."
#   Call:    truncate_string("Short")
#   Returns: "Short"

def truncate_string(string):
    if len(string) > 10:
        return f"{string[0:10]}..."
    return string

print(truncate_string("This is a long string"))
print(truncate_string("Short"))