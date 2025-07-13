# --------------------------------------
#     DELETING DATA FROM A LIST
# --------------------------------------

# Sample lists
fruit = ['orange', 'apple', 'banana', 'kiwi']
fruit1 = ['orange', 'apple', 'banana', 'kiwi']

# --------------------------
#        pop() Method
# --------------------------

# Removes and returns the last item by default
fruit.pop()
print("After pop (default removes last):", fruit)

# Removes item at a specific index
fruit1.pop(0)
print("After pop(0):", fruit1)

print('--------------------------------------------1')

# --------------------------
#        del Statement
# --------------------------

fruit = ['orange', 'apple', 'banana', 'kiwi']
del fruit[1]  # Deletes item at index 1 ('apple')
print("After del index 1:", fruit)

print('--------------------------------------------2')

# --------------------------
#        remove() Method
# --------------------------

# Removes the first matching value, not based on index
fruit = ['orange', 'apple', 'banana', 'kiwi']
fruit.remove('banana')  # Deletes 'banana'
print("After remove('banana'):", fruit)
