import datetime

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

class Animal():
    def __init__(self):
        pass

animal = Animal()
print(animal)
    

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

class Vehicle():
    def __init__(self):
        pass

vehicle = Vehicle()
print(vehicle)


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

class Cat():
    def __init__(self):
        pass

    def speak(self):
        return "miaow"

cat = Cat()
print(cat.speak())


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

class Dog():
    def __init__(self):
        pass

    def speak(self):
        return "woof"
    
dog = Dog()
print(dog.speak())


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

class StringFormatter():
    def __init__(self):
        pass

    def block_caps(self, string):
        return string.upper()
    
    def lower_case(self, string):
        return string.lower()
    
string_formatter = StringFormatter()
print(string_formatter.block_caps('hello'))
print(string_formatter.lower_case('HELLO'))


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

class Calculator():
    def __init__(self):
        pass

    def add(self, x, y):
        total = x + y
        return total

    def multiply(self, x, y):
        total = x * y
        return total
    
    def subtract(self, x, y):
        total = x - y
        return total

    def divide(self, x, y):
        total = x / y
        return total

calculator = Calculator()
print(calculator.add(1, 2))
print(calculator.multiply(2, 3))
print(calculator.subtract(3, 2))
print(calculator.divide(6, 2))


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

class Apprentice():
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort

    def format_details(self):
        return f"{self.name}, {self.cohort}"

apprentice = Apprentice('Rita Smith', 'June 2030')
print(apprentice.name)
print(apprentice.cohort)
print(apprentice.format_details())


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

class Cohort():
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

    def calculate_duration(self):
        total = self.end_date - self.start_date
        return total

cohort = Cohort('June 2020', '2020-06-01', '2020-09-01')
print(cohort.name)
print(cohort.start_date)
print(cohort.end_date)
print(cohort.calculate_duration())