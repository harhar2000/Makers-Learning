# Encapsulation in Python: A Beginner's Guide

Encapsulation is a fundamental concept in object-oriented programming (OOP). It involves bundling together related data (state) and the methods (behaviour) that operate on that data into a single unit, known as a class. Encapsulation also entails controlling access to these data and methods, ensuring that only necessary parts are exposed to the outside world while protecting the rest.

## What is Encapsulation?

Encapsulation is about hiding the internal state of an object and requiring all interaction to be performed through an object's methods. This ensures that the internal representation of an object is protected from unintended interference and misuse.

## Why Use Encapsulation?

1. **Data Protection**: By restricting access to certain components, encapsulation safeguards the integrity of the data.
2. **Modularity**: Encapsulation allows you to compartmentalise code, making it easier to manage and understand.
3. **Maintainability**: Encapsulated code is easier to maintain and less prone to errors since changes to the internal implementation do not affect external code.
4. **Flexibility**: It allows you to change the internal workings of a class without affecting other parts of the programme that rely on it.

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

- `name` is a public attribute, accessible directly using the object of the class.
- `__age` is a private attribute (indicated by the double underscore `__`), which cannot be accessed directly from outside the class.

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

- **Validation and Control**: The class controls how the data is modified, ensuring that it remains consistent and valid throughout the programme.

- **Improved Maintainability**: By encapsulating data and behaviour, your code becomes more modular and easier to maintain.

## Conclusion

Encapsulation is a powerful feature in Python that helps protect data and ensure it is used in a controlled and predictable manner. By using private attributes and providing public methods to access and modify these attributes, you can make your code more robust, secure, and easier to maintain.
