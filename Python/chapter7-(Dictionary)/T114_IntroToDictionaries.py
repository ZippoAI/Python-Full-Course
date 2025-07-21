# ----------------------- Python Dictionary Notes ------------------------

# 1. Creating a Dictionary
user = {'name': 'Bulbul', 'age': 19}
print(user)

# 2. Another way to create a dictionary using the dict() function
user1 = dict(name='zippo', age=19)
print(user1['name'])

# 3. Accessing dictionary values
print('age:', user['age'])

# 4. Dictionary with multiple data types, including lists
userInfo = {
    'Name': 'Zippo',
    'Age': 21,
    'Country': 'India',
    'Fav-Movie': ['Spider-Man', 'Iron-Man', 'Bat-Man'],
    'Fav-Fruit': ['Orange', 'Watermelon', 'Litchi']
}
print(userInfo['Fav-Movie'])

# 5. Dictionary inside a Dictionary (Nested Dictionary)
print("----------Dictionary inside Dictionary-------------")

users = {
    'user1': {
        'Name': 'Zippo',
        'Age': 21,
        'Country': 'India',
        'Fav-Movie': ['Spider-Man', 'Iron-Man', 'Bat-Man'],
        'Fav-Fruit': ['Orange', 'Watermelon', 'Litchi']
    },

    'user2': {
        'Name': 'Zippo',
        'Age': 21,
        'Country': 'India',
        'Fav-Movie': ['Spider-Man', 'Iron-Man', 'Bat-Man'],
        'Fav-Fruit': ['Orange', 'Watermelon', 'Litchi']
    }
}

# Accessing nested dictionary values
print(users['user1']['Name'])

# 6. Adding and updating values in a dictionary
user_info = {}
user_info['name'] = 'Bulbul'     # Adding a new key-value pair
user_info['name'] = 'ZIPPO77'    # Updating an existing key's value

# Updating value inside nested dictionary
users['user1']['Name'] = 'Alkama'
print(users['user1']['Name'])

# Display final updated user_info
print(user_info)

# -----------------------------------------------------------------------
# Summary:
# - Dictionaries are created using {} or dict()
# - Keys must be unique and immutable (like strings or numbers)
# - Values can be of any data type (string, list, even another dictionary)
# - You can add, update, and access values using keys
# - Nested dictionaries are useful for storing structured data
