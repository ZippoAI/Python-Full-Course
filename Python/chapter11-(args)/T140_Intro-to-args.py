# 🧠 Intro to *args in Python

# *args lets you pass a variable number of **positional arguments** into a function.
# These arguments are collected into a tuple called 'args'.

# ✅ It's useful when you're not sure how many inputs you'll receive.

# Example:

def all_total(*args):
    """
    Returns the sum of all values passed as positional arguments.
    args will be a tuple like: (1, 2, 3, 4, 5, 10)
    """
    total = 0
    for i in args:
        total += i
    return total

# Calling the function with 6 arguments
print(all_total(1, 2, 3, 4, 5, 10))  # Output: 25
