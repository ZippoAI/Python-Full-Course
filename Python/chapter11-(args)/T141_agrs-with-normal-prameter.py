# 📝 *args in Python

# *args allows a function to accept any number of **positional arguments**.
# These extra arguments are stored as a tuple.

# ✅ Useful when you don't know how many inputs the user might give.

# ------------------------------
# Example 1: Only *args used
# ------------------------------

def multiply_nums(*args):
    """
    Multiplies all numbers passed as positional arguments.
    args will be a tuple: (1, 2, 3, 4)
    """
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(1, 2, 3, 4))  # Output: 24


# ------------------------------
# Example 2: Normal parameter + *args
# ------------------------------

def show_and_multiply(msg, *args):
    """
    The first argument goes to 'msg',
    and the rest go into 'args' as a tuple.
    """
    print("Message:", msg)
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

# 'Hello' goes to msg
# (2, 3, 4) go to *args
print(show_and_multiply("Hello", 2, 3, 4))  # Output: Hello\n24

# 🔸 Important Rule:
# - If a function has both a normal parameter and *args,
#   the first argument will go to the normal one,
#   and the remaining will go to *args.
