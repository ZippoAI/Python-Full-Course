# --------------------------------------
#         LIST METHODS IN PYTHON
# --------------------------------------

# --------------------------
#        append() Method
# --------------------------

# Adds a new element to the end of the list
fruits = ['apple', 'orange']
fruits.append('banana')  # Adds 'banana' at the end
print("After append:", fruits)

# Creating an empty list and appending items
fruits = []
fruits.append('mango')
fruits.append('banana')
print("Appended to empty list:", fruits)

# --------------------------
#        insert() Method
# --------------------------

# insert(index, value) adds an element at the specified position
fruits1 = ['mango', 'apple', 'banana']
fruits1.insert(0, 'orange')  # Adds 'orange' at index 0
print("After insert:", fruits1)

# --------------------------
#        Joining Lists
# --------------------------

# 1. Using + Operator (creates a new list)
fruits2 = ['grapes', 'guava']
joined_list = fruits1 + fruits2
print("Joined using '+':", joined_list)

# 2. Using extend() Method (modifies the first list in-place)
car1 = ['audi', 'bmw']
car2 = ['tata', 'pagani']
car1.extend(car2)  # Adds elements of car2 to car1
print("After extend (car1):", car1)
print("Original car2 remains unchanged:", car2)
