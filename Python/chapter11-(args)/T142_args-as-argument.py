# 📝 Passing a List to *args Function in Python

# *args allows you to pass any number of positional arguments.
# But if you pass a list directly, it will be treated as a **single argument** (a tuple with one list inside).

# ------------------------------
# Example: Passing values directly
# ------------------------------

def multiply_nums(*args):
    multiply = 1
    print("args =", args)  # Shows how args looks
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(1, 2, 4))  # Output: 8 and args = (1, 2, 4)


# ------------------------------
# Example: Passing a list
# ------------------------------

nums = [2, 3, 4]

# ❌ Wrong: Passing list directly (it's treated as one item)
print(multiply_nums(nums))  
# Output: TypeError if trying to multiply a list by int, or wrong result
# args = ([2, 3, 4],)

# ✅ Correct: Use * to unpack the list
print(multiply_nums(*nums))  
# Output: 24 and args = (2, 3, 4)

# 🔸 Note:
# - The * before a list unpacks its elements as separate arguments.
# - This is necessary when passing a list to a *args function.
