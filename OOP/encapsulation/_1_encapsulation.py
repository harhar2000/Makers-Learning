# Encapsulation 
#   Bundling related data (attributes) and methods (functions) operating on that data into single class


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def display_info(self):
        print(f"Name : {self.name}, Age: {self.__age} ")

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")


person1 = Person("Alice", 30)
person2 = Person("Spongebog", 43)

print(person1.name)
print(person1.get_age())
person1.set_age(35)
print(person1.get_age())

print(person2.name)
print(person2.get_age())