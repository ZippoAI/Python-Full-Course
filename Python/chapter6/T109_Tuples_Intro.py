# Chapter 1 - Introduction to Tuples in Python

# What is a Tuple?
# - Tuple is an ordered collection of items.
# - Tuple is immutable (cannot change after creation).
# - Tuple allows duplicate values.
# - Tuple is faster than list because it is fixed and smaller.

example = ('one', 'two', 'three')
#No append , no insert, no pop, no remove

#Methods can be used on tuples
# Count, index
#len function
#slicing

print(example[0:2])

# How to create a Tuple:

# Creating a tuple
my_tuple = (1, 2, 3)

# Tuples are immutable - you can't change their values
# my_tuple[0] = 10  # ❌ This will cause an error

# Tuples can contain different data types
mixed_tuple = (1, "Hello", 3.5, True)

# You can access elements by index
print(mixed_tuple[1])  # Output: Hello

# Tuple unpacking
a, b, c = (10, 20, 30)
print(a, b, c)  # Output: 10 20 30

# Tuples support slicing
print(my_tuple[1:])  # Output: (2, 3)

# You can loop through a tuple
for item in my_tuple:
    print(item)

# Tuples can be nested
nested = (1, (2, 3), 4)
print(nested[1][0])  # Output: 2

# Use len() to get the number of elements
print(len(my_tuple))  # Output: 3

# You can use tuples as dictionary keys (because they are immutable)
my_dict = {(1, 2): "value"}
