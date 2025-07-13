# ===============================
# 🚀 Topic: Add and Delete Data in Python Dictionaries
# ===============================

# ✅ Creating a dictionary with user information
user_info2 = {
    'name': 'Zippo',
    'age': 21,
    'fav_fruits': ['Mango', 'Orange', 'Kiwi'],
    'fav_movies': ['Spider-Man', 'Super-Man', 'Batman-Man']
}

# ✅ Creating another dictionary with more information
more_info = {
    'state': 'Assam',
    'Country': 'India'
}

# ✅ Updating the original dictionary with new key-value pairs
user_info2.update(more_info)

# ✅ Printing the updated dictionary
print(user_info2)

# Output:
# {
#     'name': 'Zippo',
#     'age': 21,
#     'fav_fruits': ['Mango', 'Orange', 'Kiwi'],
#     'fav_movies': ['Spider-Man', 'Super-Man', 'Batman-Man'],
#     'state': 'Assam',
#     'Country': 'India'
# }
