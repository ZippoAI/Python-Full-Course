# -----------------------------
# 📌 ZIP FUNCTION IN PYTHON
# -----------------------------

# ✅ The zip() function is used to combine two or more iterables (like lists, tuples) element-wise.
# ✅ It returns an iterator of tuples.
# ✅ If iterables are of different lengths, zip() stops at the shortest one.

# 📌 Basic Example
names = ["Zippo", "Odin", "Rhynamo"]
marks = [88, 92, 79]

zipped = zip(names, marks)
print(list(zipped))  # [('Zippo', 88), ('Odin', 92), ('Rhynamo', 79)]

# 📌 zip() with 3 or more lists
ages = [21, 22, 23]

zipped_3 = zip(names, marks, ages)
print(list(zipped_3))  # [('Zippo', 88, 21), ('Odin', 92, 22), ('Rhynamo', 79, 23)]

# 📌 Converting zip object to dictionary
name_mark_dict = dict(zip(names, marks))
print(name_mark_dict)  # {'Zippo': 88, 'Odin': 92, 'Rhynamo': 79}

# 📌 Unzipping a zipped list
zipped_list = [('Zippo', 88), ('Odin', 92), ('Rhynamo', 79)]
names_unzipped, marks_unzipped = zip(*zipped_list)

print(list(names_unzipped))  # ['Zippo', 'Odin', 'Rhynamo']
print(list(marks_unzipped))  # [88, 92, 79]

# 📌 zip() with map()
a = [10, 20, 30]
b = [1, 2, 3]

added = list(map(lambda x: x[0] + x[1], zip(a, b)))
print(added)  # [11, 22, 33]

# 📌 zip() with filter()
filtered = list(filter(lambda pair: pair[1] > 90, zip(names, marks)))
print(filtered)  # [('Odin', 92)]

# ⚠️ zip() stops at shortest iterable
a = [1, 2, 3]
b = [10, 20]

print(list(zip(a, b)))  # [(1, 10), (2, 20)]

# 📌 Looping with zip()
for name, mark in zip(names, marks):
    print(f"{name} scored {mark}")

# ---------------------------------------------------
# 🧪 CUSTOM EXAMPLE – User IDs and Names Assignment
# ---------------------------------------------------

# Zip Function
user_id = ['user1', 'User2', 'User3']
names = ['Zippo', 'Bulbul', 'Bulbul']

# now if we want to assign the user_id to the names we can use zip()
combined = list(zip(user_id, names))
print(combined)
# Output: [('user1', 'Zippo'), ('User2', 'Bulbul'), ('User3', 'Bulbul')]

# iterating through zipped pairs
for key, value in combined:
    print(f'{key}: {value}')

# ⚠️ What if one list is shorter?

user_id2 = ['user1', 'User2']
names2 = ['Zippo', 'Bulbul', 'Bulbul']

# here when one of the smaller list ends, zip() will stop
combined2 = list(zip(user_id2, names2))
print(combined2)
# Output: [('user1', 'Zippo'), ('User2', 'Bulbul')]
