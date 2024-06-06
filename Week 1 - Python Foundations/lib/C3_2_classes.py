
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

class Greeter():
     def __init__(self, name):
         self.name = name
     def say_hello(self):
         return 'Hello, ' + self.name + '!'
     def say_goodbye(self):
         return 'Goodbye, ' + self.name + '!'
     def say_goodnight(self):
         return 'Goodnight, ' + self.name + '!'
     def say_goodmorning(self):
         return 'Good Morning, ' + self.name + '!'
     
greeter = Greeter('Bobby')
print(greeter.say_hello())
print(greeter.say_goodbye())
print(greeter.say_goodnight())
print(greeter.say_goodmorning())


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

class Basket():
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def list_items(self):
        return self.items
    
basket = Basket()
basket.add('apple')
basket.add('banana')
basket.add('orange')
print(basket.list_items())


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

class Calculator():
    def __init__(self):
        self.record = []

    def add(self, x, y):
        total = x + y
        self.record.append(total)
        return total
    
    def multiply(self, x, y):
        total = x * y
        self.record.append(total)
        return total
    
    def subtract(self, x, y):
        total = x - y
        self.record.append(total)
        return total
    
    def divide(self, x, y):
        total = x / y
        self.record.append(total)
        return total
    
    def list_history(self):
        return self.record

calculator = Calculator()
print(calculator.add(1, 2))
print(calculator.multiply(3, 4))
print(calculator.subtract(5, 6))
print(calculator.divide(7, 8))
print(calculator.list_history())


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

class Cohort():
    def __init__(self):
        self.student_list = []

    def add_student(self, dict):
        self.student_list.append(dict)

    def list_students(self):
        return self.student_list
    
    def list_employed_by(self, employer):
        return [student for student in self.student_list if student['employer'] == employer]

cohort = Cohort()
cohort.add_student({'name' : 'Jo', 'employer' : 'NASA'})
cohort.add_student({'name' : 'Alex', 'employer' : 'NASA'})
cohort.add_student({'name' : 'Bobby', 'employer' : 'Google'})
print(cohort.list_students())
print(cohort.list_employed_by('NASA'))


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

class Person():
    def __init__(self, dict):
        self.name = dict.get('name', '')
        self.pets = dict.get('pets', [])
        self.addresses = dict.get('addresses', [])
        self.work_address = next((addr for addr in self.addresses if addr['name'] == 'work'), None)
        self.home_address = next((addr for addr in self.addresses if addr['name'] == 'home'), None)

    def get_work_address(self):
        if self.work_address:
            return f"{self.work_address['building']} {self.work_address['street']}"
        return "No work address available"
    
    def get_home_address(self):
        if self.home_address:
            return f"{self.home_address['building']} {self.home_address['street']}"
        return "No home address available"
    
    def get_pets(self):
        pet_descriptions = ', '.join([f"a {pet['animal']} called {pet['name']}" for pet in self.pets])
        return f'{self.name} has no pets' if not self.pets else f'{self.name} has {len(self.pets)} pets: {pet_descriptions}'

data = {
    'name': 'Alex',
    'pets': [
        {'name': 'Arthur', 'animal': 'cat'},
        {'name': 'Judith', 'animal': 'dog'},
        {'name': 'Gwen', 'animal': 'goldfish'}
    ],
    'addresses': [
        {'name': 'work', 'building': '50', 'street': 'Commercial Street'},
        {'name': 'home', 'building': '10', 'street': 'South Street'}
    ]
}

person = Person(data)
print(person.get_work_address())
print(person.get_home_address())
print(person.get_pets())