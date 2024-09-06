# # Python OOP Practice Questions
# Beginner Level

# 1. Create a Book class:
# - Define a Book class with attributes like title, author, and __price.
# - Implement a method to display the book details.
# - Implement getter and setter methods for the __price attribute, ensuring the price is always positive.




# book1 = Book("1984", "George Orwell", 10.99)
# book1.display_details(book1.title, book1.author, book1.get_price())
# print(f"Initial Price: £{book1.get_price()}")
# book1.set_price(12.99)
# print(f"Updated Price: £{book1.get_price()}")
# book1.set_price(-5.00)  # This should print a warning
# book1.display_details(book1.title, book1.author, book1.get_price())




# 2. Implement a Rectangle class:
# - Create a Rectangle class with private attributes __length and __width.
# - Write methods to calculate the area and perimeter of the rectangle.
# - Provide getter and setter methods for the __length and __width, ensuring they are positive numbers.





# rect = Rectangle(10, 5)
# print("Area:", rect.calc_area())  # Output should be 50
# print("Perimeter:", rect.calc_perimeter())  # Output should be 30
# print("Length:", rect.get_length())  # Output should be 10
# print("Width:", rect.get_width())  # Output should be 5

# rect.set_length(15)
# rect.set_width(7)

# print("New Area:", rect.calc_area())  # Output should be 105
# print("New Perimeter:", rect.calc_perimeter())  # Output should be 44

# rect.set_length(-5)  # Should print "Length must be above 0"






# 3. Create a Student class:
# - Define a Student class with attributes name and __grade.
# - Implement a method to determine if the student has passed or failed based on the grade (pass mark is 50).
# - Provide methods to get and set the __grade, with validation that the grade must be between 0 and 100.






# student1 = Student("Alice", 85)
# print(f"{student1.name}'s grade: {student1.get_grade()}")  # Output: Alice's grade: 85
# print(f"Did {student1.name} pass? {student1.pass_or_fail()}")  # Output: Did Alice pass? Pass
# student1.set_grade(45)
# print(f"{student1.name}'s updated grade: {student1.get_grade()}")  # Output: Alice's updated grade: 45
# print(f"Did {student1.name} pass? {student1.pass_or_fail()}")  # Output: Did Alice pass? Fail
# student1.set_grade(150)  # Output: Grade must be between 0 and 100

# student2 = Student("Bob", 30)
# print(f"{student2.name}'s grade: {student2.get_grade()}")  # Output: Bob's grade: 30
# print(f"Did {student2.name} pass? {student2.pass_or_fail()}")  # Output: Did Bob pass? Fail





# Intermediate Level

# 4. Design a BankAccount class:
# - Create a BankAccount class with attributes account_number, owner, and __balance.
# - Implement methods to deposit and withdraw money, with checks to prevent overdrafts.
# - Write a method to transfer money from one account to another, ensuring the transfer is valid.

class BankAccount:
    def __init__(self, account_number:int, owner:str, balance:float):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance

    def check_balance(self):
        return self.__balance

    def deposit(self, amount:float):
        if amount < 0:
            print("Value entered must be positive")
        else: self.__balance = self.__balance + amount
        return f"Your new balance is {self.__balance} "

    def withdraw(self, amount:float):
        if amount < 0:
            return f"Amount must be positive "
        elif amount > self.__balance:
                return f"Insufficient funds. You have {self.__balance} in your account."
            
        self.__balance -= amount
        return f"You withdrew {amount}. Your new balance is {self.__balance}"
        
    def transfer_money(self, Target_account, bankaccount,):
        # transfer amount must not be more than available balance
        # ensure other account is valid - it should be another instance of BankAccount
        # withdraw from one account
        # deposit in another

 








# 5. Implement a Car class:
# - Define a Car class with attributes like make, model, year, and __mileage.
# - Provide methods to update the mileage and calculate the car's age.
# - Ensure the mileage can only increase and not decrease.





# 6. Create a Library class:
# - Create a Library class that manages a collection of books (hint: use the Book class from the first question).
# - Implement methods to add a book, remove a book, and search for a book by title.
# - Implement a method to list all books in the library.




# Advanced Level

# 7. Design a Temperature class:
# - Create a Temperature class with attributes for Celsius and Fahrenheit, but only store one internally (e.g., Celsius).
# - Implement methods to convert between Celsius and Fahrenheit.
# - Provide getter and setter methods that automatically convert between the two units, maintaining consistency.





# 8. Implement a University class:
# - Create a University class that manages a list of students (use the Student class from earlier).
# - Implement methods to add and remove students, calculate the average grade, and find the top-performing student.
# - Encapsulate the student list to prevent direct access from outside the class.





# 9. Create a ShoppingCart class:
# - Define a ShoppingCart class that holds a list of items, each with a name, price, and quantity.
# - Implement methods to add items, remove items, and calculate the total cost of the cart.
# - Include a method to apply a discount code that reduces the total cost by a percentage.





# 10. Build a Course class:
# - Create a Course class with attributes like course_name, instructor, and a private list of students enrolled.
# - Implement methods to enroll and drop students, check if a student is enrolled, and get the total number of students.
# - Ensure that a student cannot be enrolled more than once and cannot be dropped if they are not enrolled.




# Extra Challenges

# 11. Implement a SecureVault class:
# - Create a SecureVault class that stores sensitive information (e.g., passwords).
# - Implement methods to securely add, retrieve, and delete information.
# - Ensure that the information is encrypted before being stored and decrypted when retrieved.






# 12. Create a Company class:
# - Define a Company class with attributes like name, industry, and a private list of employees.
# - Implement methods to hire, fire, and list employees.
# - Implement a method to calculate the average salary of the employees, ensuring salaries are encapsulated and validated.




# Beginner Level Answers

# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.__price = price

#     def get_price(self):
#         return self.__price
    
#     def set_price(self, price):
#         if price > 0:
#             self.__price = price

#     def display_details(self, title, author, price):
#         print(f"{title}: by {author},  £{price}")








# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width

#     def calc_area(self):
#         return self.__length * self.__width

#     def calc_perimeter(self):
#         return 2 * (self.__length + self.__width)

#     def get_length(self):
#         return self.__length

#     def set_length(self, length):
#         if length > 0:
#             self.__length = length
#         else:
#             print("Length must be above 0") 

#     def get_width(self):
#         return self.__width

#     def set_width(self, width):
#         if width > 0:
#             self.__width = width
#         else:
#             print("Length must be above 0") 






# class Student:
#     def __init__(self, name:str, grade):
#         self.name = name
#         self.__grade = grade

#     def get_grade(self):
#         return self.__grade

#     def set_grade(self, grade):
#        if 0 <= grade <= 100:
#            self.__grade = grade
#        else:
#            print("Grade must be between 0 and 100")

#     def pass_or_fail(self):
#         if self.__grade <= 50:
#             return "Fail"
#         else:
#             return "Pass"