# Encapsulation in Python: A Beginner's Guide

Encapsulation is a key concept in object-oriented programming (OOP). It refers to the practice of bundling related data (attributes) and the methods (functions) that operate on that data within a single unit known as a class. Encapsulation also restricts direct access to some of an object's components, ensuring that only essential parts are exposed to the outside world while protecting the rest

Encapsulation hides the internal state of an object and makes sure all interactions happen through specific methods. This protects the object's data from being accidentally changed or misused.

## Why Use Encapsulation?

1. **Protects Data**: Keeps certain parts of your code private, ensuring that data can't be changed accidentally.
2. **Keeps Code Organised**: Helps break down code into manageable sections, making it easier to read and work with.
3. **Maintainability**: Simpifies updates and reduces likelihood of causing issues as internal workings of a class are hidden from other parts of your program. This abstraction allows you to change the internal implementation without affecting code that relies on the class.
4. **Flexibility**: Can modify how a class works internally without disrupting the rest of your code that depends on it.

## Basic Example of Encapsulation

Consider a simple example to understand encapsulation in Python.

```python
class Person:
    def __init__(self, name, age):
        self.name = name    # Public attribute
        self.__age = age    # Private attribute

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.__age}")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

# Create an object of Person
person1 = Person("Alice", 30)

# Accessing public attribute
print(person1.name)  # Output: Alice

# Trying to access private attribute directly will raise an error
# print(person1.__age)  # This will raise an AttributeError

# Accessing private attribute through a method
print(person1.get_age())  # Output: 30

# Modifying private attribute through a method
person1.set_age(35)
print(person1.get_age())  # Output: 35

# Attempting to set an invalid age
person1.set_age(-5)  # Output: Age must be positive
```

### Explanation of the Example

#### Public and Private Attributes:

- `name` is a public attribute, it can be accessed and modified from anywhere in and out the class
- `__age` is a private attribute (indicated by the `__`), which cannot be accessed or modified directly from outside the class. We use this to protect sentitive data.

    ##### When to Use Public Attributes

    - When the attribute is part of the object's interface and you want it to be easily accessible.
    - When you don’t need to enforce strict control over how the attribute is used or modified.

    ##### When to Use Private Attributes

    - When you need to protect the attribute from being accessed or modified directly.
    - When you want to hide the implementation details of a class.
    - When you need to enforce rules or conditions whenever the attribute is accessed or modified.

#### Methods for Accessing Private Data:

- `get_age()` and `set_age(age)` are public methods provided to access and modify the private attribute `__age`.

#### Data Validation:

- The `set_age(age)` method includes a simple validation to ensure the age is positive. This ensures that the `__age` attribute is not set to an invalid value.

### Encapsulation in Action

Here’s another example where encapsulation proves useful:


```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

# Create a bank account
account = BankAccount("John Doe", 1000)

# Deposit money
account.deposit(500)  # Output: Deposited 500. New balance is 1500

# Withdraw money
account.withdraw(300)  # Output: Withdrew 300. New balance is 1200

# Attempt to withdraw more than the balance
account.withdraw(2000)  # Output: Insufficient balance or invalid amount

# Access balance via a method
print(account.get_balance())  # Output: 1200

# Direct access to __balance is not allowed
# print(account.__balance)  # This will raise an AttributeError
```


## Key Points

- **Encapsulation allows the class to hide its data**: In the examples, the balance is hidden and can only be accessed or modified through the provided methods (`deposit`, `withdraw` and `get_balance`).

- **Validation and Control**: The class controls how the data is modified, ensuring that it remains consistent and valid throughout the program.

- **Improved Maintainability**: By encapsulating data and behaviour, your code becomes more modular and easier to maintain.

## Conclusion

Encapsulation is a powerful feature in Python that helps protect data and ensure it is used in a controlled and predictable manner. By using private attributes and providing public methods to access and modify these attributes, you can make your code more robust, secure, and easier to maintain. Encapsulation works hand in hand with other OOP principles like inheritance and polymorphism, contributing to the creation of modular, scalable and flexible code.