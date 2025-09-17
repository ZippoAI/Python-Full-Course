
# ---------------- Encapsulation ----------------
# Encapsulation is the concept of wrapping data (variables) and methods into a single unit (class),
# and restricting direct access to some of the object's components.
# Example:

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.__price = price  # Private attribute (encapsulated)

    def make_a_call(self, phone_number):
        print(f"Calling {phone_number}.......")

    def full_name(self):
        return f"{self.brand} - {self.model_name}"

    def get_price(self):
        # Public method to access private attribute
        return self.__price

    def set_price(self, new_price):
        # Setter method with validation
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive!")


# Usage of Encapsulation
phone1 = Phone('Iphone', '14 Pro', 200)
print(phone1.full_name())
print("Price:", phone1.get_price())  # Accessing private attribute via method
phone1.set_price(-100)  # Invalid price
phone1.set_price(250)
print("Updated Price:", phone1.get_price())

# Direct access to __price is not allowed:
# print(phone1.__price)  # AttributeError

# ---------------- Name Mangling ----------------
# Name Mangling is a mechanism where Python internally changes the name of private variables
# to prevent accidental access. For example, __price becomes _Phone__price.
print("Accessing mangled name:", phone1._Phone__price)  # Not recommended, but possible

# ---------------- Naming Convention ----------------
# _name      : Convention for 'protected' (internal use) attributes
# __name     : Name mangling for 'private' attributes
# __name__   : Dunder (double underscore) methods, e.g., __init__, __str__

class Example:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected (by convention)"
        self.__private = "I am private (name mangled)"

    def __str__(self):
        return self.public

e = Example()
print(e.public)
print(e._protected)
# print(e.__private)  # AttributeError
print(e._Example__private)  # Access via name mangling

# ---------------- Abstraction ----------------
# Abstraction means hiding complex implementation details and showing only the necessary features.
# In Python, abstraction is often achieved using abstract base classes (ABC) and methods.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started!")

my_car = Car()
my_car.start()
# v = Vehicle()  # TypeError: Can't instantiate abstract class

# Built-in abstraction example:
l = [6,5,3,4,1,2]
l.sort()  # We use sort() without knowing the internal algorithm (abstraction)
print("Sorted list:", l)

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand 
        self.model_name = model_name
        # self.price = price
        self.__price = price

    
    def make_a_call(self, phone_number):
        print(f"Calling {phone_number}.......")

    def full_name(self):
        return f"{self.brand} - {self.model_name}"
    

# ----------NAMING CONVENTION--------------
# _name #Convention for private property
# __name__ # dunder / magic method


#Abstraction
l = [6,5,3,4,1,2]
l.sort() # tim sort 
print(l)



phone1 = Phone('Iphone', '14 Pro', 200)
phone2 = Phone('Samsung', 'Galaxy Pro', 100)
phone3 = Phone('IPad', 'M4', 400)

print(phone1._Phone__price)

print(phone1.__dict__)
# phone1._price = -200
# print(phone1._price)

# print(phone1.make_a_call(12312321))