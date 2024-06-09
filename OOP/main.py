import datetime
from email.policy import HTTP

from psutil import users

# Without Inheritance

# This section defines different classes for people of different nationalities without using inheritance.
# Each class has its own implementation of the say_hello method, resulting in code duplication.

class AmericanPerson():
    def say_hello():
        return "Hey pal, how are you?"
    
class GermanPerson():
    def say_hello():
        return "Hallo, Guten Tag!"
    
class SpanishPerson():
    def say_hello():
        return "Buenos Dias!"
    
class EnglishPerson():
    def say_hello():
        return "Hey pal, how are you?"
    
class AustralianPerson():
    def say_hello():
        return "Hey pal, how are you?"
    
# With Inheritance
# Inheritance reduces code duplication.
# Base class Person with say_hello() method is created.
# Specific person classes inherit from Person.

class Person():
    def __init__(self, name):
        self.name = name 

    def say_hello(self):
        return "Hey pal, how are you?"

class AmericanPerson(Person):
    pass

class EnglishPerson(Person):
    pass

class AustralianPerson(Person):
    pass


# Polymorphism 
# GermanPerson class overrides say_hello method from Person class, demonstrating polymorphism. 
# This allows GermanPerson to provide its own specific implementation of the method.

class GermanPerson(Person):
    def say_hello(self):
        return "Hallo, Guten Tag!"
    
# ___________________________________________________________


# Abstraction and Encapsulation

# WriteObject class encapsulates details about the type of writing object.
# Notebook class encapsulates logic of writing with different types of writing objects using private methods.

class WriteObject():
    def __init__(self, type):
        self.type = type
        
class Notebook():
    def __init__(self, write_object):
        self.write_object = write_object

    def write(self, write_object, text):
        if write_object.type == "ball pen":
            self.__turn_on(write_object)
            return text 
        
        elif write_object.type == "ink pen":
            if self.__has_enough_ink(write_object):
                return text
            else:
                self.__refill_ink(write_object)
                return text
            
        elif write_object.type == "pencil":
            if self.__sharp_enough(write_object):
                return text
            else:
                self.__sharpen(write_object)
                return text
        else:
            return "need some write object to write"
        
# private functions
    def __sharpen(write_object):
        pass

    def __refill_ink(write_object):
        pass

    def __sharp_enough(write_object):
        pass

    def __has_enough_ink(write_object):
        pass

    def __turn_on(write_object): # press top of ball pen to turn it on 
        pass 

write_object = WriteObject('pencil')
notebook = Notebook(write_object)
notebook.write(notebook.write_object, "My daily memo")

## With Abstraction

# Uses abstract classes to define common interface for different writing objects.
# WriteObject class cannot be instantiated directly, forcing  use of specific subclasses like Pencil, BallPen and InkPen, which implement the write method.


class WriteObject(): # abstract
    def __init__(self):
        raise Exception('writeObject cant be instantiated')
    
    def write(self):
        raise Exception('WriteObject cant write, pls instantiate a Pencil, Ink Pen or Ball Pen')
    
class Pencil(WriteObject):
    def __init__(self):
        pass

    def write(self, text):
        if self.__sharp_enough():
            return text
        else:
            self.__sharpen()
            return text
        
    # Private
    def __sharp_enough(self): 
        # Check if pencil is sharp enough
        pass

    def __sharpen(self):
        #sharpen pencil
        pass

class BallPen(WriteObject): 
    def __init__(self):
        pass

    def write(self, text):
        self.__turn_on()
        return text
    
    # Private
    def __turn_on():
        #turn on pen
        pass  

class InkPen(WriteObject): 
    def __init__(self):
        pass

    def write(self, text):
        if self.__has_enough_ink():
         return text 
        else:
            self.__refill_ink()
            return text
        
    # private

    def __has_enough_ink(self):
        #check if there is enough ink
        pass

    def __refill_ink(self):
        # refill ink
        pass

# Notebook class uses polymorphism to interact with different writing objects through a common interface.
# BallPen, InkPen and Pencil

class Notebook():
    def __init__(self, write_object):
        self.write_object = write_object
    
    def write(self,text):
        return self.write_object.write(text)



## Enapsulation
# Shows encapsulation by hiding internal state and implementation details of MobilePhone class. Methods for accessing and modifying memory and for launching applications.


class MobilePhone():
    def __init__(self, memory: int, cores: int, colour: str):
        self.__memory = memory
        self.__cores = cores
        self.__colour = colour

    def get_memory(self):
        return self.__memory

def launch_application(self, application):
    self.__start_application(self.__memory / 10, application)

def __set_memory(self, memory):
    self.__memory = memory

def __start_application(self, memory_count, application):
    # allocate memory_count and start application
    pass

# Exclusion
# Provides basic implementation of Post class without any encapsulation, abstraction, inheritance or polymorphism. 
# Directly exposes its attributes.

class Post():
    def __init__(self, id, content):
        self.id = id
        self.content = content


# SOLID Principles
## Single Responsibility principle        - Responsible for only one thing
## Open/Closed principle                  - functions/classes/objects are open for extention but closed for modification
## Liskov's segregation principle         - Child object can replace parent object anytime without breaking application 
## Interface segregation principle
## Dependency Inversion princple



## Single Responsibility principle

### not singularly responsible 
### singularly responsible 

class Account():
    # only the accounts in the business are responsible for requiring features for the Account object
    pass

#### 

class Transaction():
    def __init__(self, sum, type):
        self.sum = sum
        self.type = type
        self.date = datetime.now()

class StatementPrinter():
    def __init__(self):
        return 
    
    def print_statment(self, transaction):
        # make a new statement string to store statement data
        # add header
        # iterate over transactions data
        # add transaction data for each transaction object to the string
        # add footer
        # return or print statement string
        return

class BankAccount():
    def __init__(self):
        self.balance = 0
        self.transactions = []
        self.printer = StatementPrinter()

    def withdraw(self, sum):
        # do the checks
        # make new transaction data
        # withdraw
        return 
    
    def deposit(self, sum):
        # do the checks
        # make new transaciton data
         # self.transaction.add()
        # {'type': 'deposit', 'sum':sum, 'date' : datetime.now()} new Transation(sum, type)
        # deposit
        return
    
    def print_statements(self, transaction):
        # self.printer.printer_statement(transaction)
        
        return
    
## Open / Closed princple  

## Liskov's subsitution principle

class HTTPRequest():
    pass

class HTTPResponse():
    pass

class JSONResponse(HTTPResponse):
    pass

class Application():
    users = []
    def send_response(res :HTTPResponse): #  HTTPResponse
    res.data.users = users
    return res

class SomeOtherApplication():
    def deal_with_response():
        response = JSONResponse()
        send_response(response)

## Interface Segragation principle

## Dependency Inversion principle 
