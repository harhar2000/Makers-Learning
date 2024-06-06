# == EXERCISES ==

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
def fizz_buzz(number):
    if number % 15 == 0:
        return "fizzbuzz"
    if number % 3 == 0:
        return "fizz"
    if number % 5 == 0:
        return "buzz"
    else:
        return number
    

print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(8))


# Purpose: responds to the user's greeting

# Rules:   if the greeting is 'good morning'
#          return 'good morning to you too'
#          if the greeting is 'hello'
#          return 'hi'
#          if the greeting is anything else
#          return the greeting that was received
# Example:
#   Call:    reply_to("good morning")
#   Returns: "good morning to you too"
#   Call:    reply_to("hello")
#   Returns: "hi"
#   Call:    reply_to("how are you?")
#   Returns: "how are you?"
def reply_to(greeting):
    if greeting == "good morning":
        return "good morning to you too"
    if greeting == "hello":
        return "hi"
    else: 
        return greeting

print(reply_to("good morning"))
print(reply_to("hello"))
print(reply_to("how are you?"))


# Purpose: deducts 10 from a number if it is greater than or equal to 10,
#          otherwise returns the number
# Example:
#   Call:    deduct_10_if_possible(25)
#   Returns: 15
#   Call:    deduct_10_if_possible(10)
#   Returns: 0
#   Call:    deduct_10_if_possible(9)
#   Returns: 9
def deduct_10_if_possible(number):
    if number >= 10:
        return number - 10
    else:
        return number

print(deduct_10_if_possible(25))
print(deduct_10_if_possible(10))
print(deduct_10_if_possible(9))


# Purpose: if the number is below 100, return 100, otherwise return the number
# Example:
#   Call:    top_up_to_100(25)
#   Returns: 100
#   Call:    top_up_to_100(100)
#   Returns: 100
#   Call:    top_up_to_100(125)
#   Returns: 125
def top_up_to_100(number):
    if number < 100:
        return 100
    return number

print(top_up_to_100(25))
print(top_up_to_100(100))
print(top_up_to_100(125))