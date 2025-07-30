# iterator_vs_iterable_notes.py

# =============================
#   ITERATOR vs ITERABLE in Python
# =============================

# What is an Iterable?
# ---------------------
# An object capable of returning its members one at a time.
# Examples: lists, tuples, strings, sets, dictionaries, etc.

numbers = [1, 2, 3, 4]  # This is an iterable

# You can loop through an iterable using a for loop
for i in numbers:
    print(i)

print('-----------')

# What is an Iterator?
# ---------------------
# An object representing a stream of data; returns one element at a time.
# It implements two methods: __iter__() and __next__()

# map() returns an iterator
squares = map(lambda a: a ** 2, numbers)  # This is an iterator

for i in squares:
    print(i)

print('-----------')

# How does a loop work behind the scenes?
# ----------------------------------------

# When you use a for-loop, Python internally uses the `iter()` function to get an iterator
# and calls `next()` repeatedly until StopIteration is raised.

number_iter = iter(numbers)  # Convert the iterable into an iterator

print(next(number_iter))  # Output: 1
print(next(number_iter))  # Output: 2
print(next(number_iter))  # Output: 3
print(next(number_iter))  # Output: 4

# If you call next again, it will raise StopIteration
# print(next(number_iter))  # Uncommenting this will cause StopIteration error

print('----------------')

# Summary:
# --------
# Iterable: Can be looped over (e.g. list, tuple)
# Iterator: Produces next item using next()
# Use iter() to get iterator from iterable
