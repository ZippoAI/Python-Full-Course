
"""
Property & Setter in Python (OOP)
----------------------------------
This chapter explains how to use the @property decorator and setter methods in Python classes.
These features help you control access to attributes, add validation, and keep your code clean and Pythonic.
"""

# --------------------
# 1. Why use @property?
# --------------------
# - To make a method act like an attribute.
# - To add logic (like validation) when getting or setting a value.
# - To encapsulate private data and expose a public interface.

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        # Encapsulated attribute (by convention, _price is 'protected')
        if price > 0:
            self._price = price
        else:
            self._price = 0

    # Property: allows us to access this method like an attribute
    @property
    def complete_specification(self):
        """Returns a string with all phone details."""
        return f"{self.brand} - {self.model_name} and {self._price}"

    # Getter for price
    @property
    def price(self):
        """Get the price of the phone."""
        return self._price

    # Setter for price
    @price.setter
    def price(self, new_price):
        """Set the price, ensuring it is not negative."""
        self._price = max(new_price, 0)

    def make_a_call(self, phone_number):
        print(f"Calling {phone_number}.....")


    def full_name(self):
        return f"{self.brand} {self.model_name}"

# Usage Example:
phone1 = Phone('Iphone', '15 Pro Max', 200)

# Accessing public attributes
print("Brand:", phone1.brand)
print("Model:", phone1.model_name)
# Accessing protected attribute (not recommended outside class)
print("_price (protected):", phone1._price)
print('-----------')

# Using the property getter and setter
phone1.price = 500  # Calls the setter
print("Price (via property):", phone1.price)  # Calls the getter
print("Complete specification:", phone1.complete_specification)
print("Full name:", phone1.full_name())

# Validation example
phone1.price = -100  # Will set price to 0 due to validation in setter
print("After setting negative price:", phone1.price)

# --------------------
# 2. Benefits of @property
# --------------------
# - Cleaner syntax: obj.attr instead of obj.get_attr()
# - Backward compatibility: You can start with a public attribute, then later add logic without changing the interface.
# - Encapsulation: Hide internal details, expose only what you want.

# --------------------
# 3. Real-world Example
# --------------------
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

item = Product("Book", 100)
print("\nProduct price:", item.price)    # 100
item.price = 120     # Valid
print("Updated product price:", item.price)
# item.price = -10   # Raises ValueError

# --------------------
# 4. Summary
# --------------------
# - Use @property to define managed attributes.
# - Use @attr.setter to add validation or logic when setting values.
# - Use @attr.deleter if you need to control deletion.
# - This keeps your code clean, safe, and Pythonic!
    
