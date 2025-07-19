# -----------------------------
#        Add and Delete Data
# -----------------------------

# Initial user information stored in a dictionary
user_info = {
    'name': 'Zippo',
    'age': 21,
    'fav_movies': ['Spider-Man', 'Super-Man', 'Batman-Man'],
    'fav_fruits': ['Mango', 'Orange', 'Kiwi']
}

# -----------------------------
#        Adding Data
# -----------------------------

# Replacing 'fav_fruits' with a new list
user_info['fav_fruits'] = ['Apple', 'Banana']
print("Updated fav_fruits:", user_info['fav_fruits'])

# -----------------------------
#        Deleting Data
# -----------------------------

# Removing a specific movie from 'fav_movies'
user_info['fav_movies'].remove('Spider-Man')

# Removing the last fruit from 'fav_fruits'
user_info['fav_fruits'].pop()

print("Updated fav_movies:", user_info['fav_movies'])
print("Updated fav_fruits:", user_info['fav_fruits'])

# -----------------------------
#        popitem() Method
# -----------------------------

# New dictionary for popitem demo
user_info2 = {
    'name': 'Zippo',
    'age': 21,
    'fav_fruits': ['Mango', 'Orange', 'Kiwi'],
    'fav_movies': ['Spider-Man', 'Super-Man', 'Batman-Man'], 
}

# popitem() removes the last inserted key-value pair
popped_item = user_info2.popitem()

print("Popped item:", popped_item)
print("Remaining values in user_info2:", user_info2.values())

