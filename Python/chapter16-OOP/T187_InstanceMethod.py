'''
What is an Instance Method?

An instance method is a function defined inside a class that operates on an instance of the class. It can access and modify the object’s attributes using the self keyword.

self refers to the instance of the class that calls the method.

Instance methods are the most common type of method in Python.


Syntax:
class ClassName:
    def instance_method(self, arg1, arg2):
        # code that works with instance attributes
        pass

'''
print('----Example Start----------------')

class Person:
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute

    # instance method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    # instance method with argument
    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday! I am now {self.age} years old.")

# Create instance
p1 = Person("Alice", 25)

# Call instance methods
p1.greet()         # Hello, my name is Alice and I am 25 years old.
p1.have_birthday() # Happy Birthday! I am now 26 years old.

print('-----------------Example End-----------')
print()
# Instance methods

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.age}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

p1 = Person('Bulbul', 'Hassan', 21)

print(p1)

print(p1.full_name())


# Clear Method
l = [1,2,3,4,5]

# l.clear()
list.clear(l)
print(l)
print('---------------------cleared-----------------')


l = [1, 2, 3]
list.append(l, 4) 
print(l)  # [1, 2, 3, 4]
