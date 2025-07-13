# ------------------- PYTHON DICTIONARY: PART 2 -----------------------

userInfo = {
    'Name': 'Zippo',
    'Age': 21,
    'Country': 'India',
    'Fav-Movie': ['Spider-Man', 'Iron-Man', 'Bat-Man'],
    'Fav-Fruit': ['Orange', 'Watermelon', 'Litchi']
}

# ✅ 1. CHECK IF A KEY EXISTS IN A DICTIONARY
if 'Name' in userInfo:
    print('Key Found:', userInfo['Name'])
else:
    print('Key Not Found')

# ✅ 2. CHECK IF A VALUE EXISTS IN A DICTIONARY
if 'Zippo' in userInfo.values():
    print('Value Found')
else:
    print('Value Not Found')

# ✅ 3. LOOP THROUGH A DICTIONARY
print('----- Looping Through Dictionary -----')

# a) Print all values using values()
for value in userInfo.values():
    print('Value:', value)

# b) Print all values using keys
for key in userInfo:
    print('Value:', userInfo[key])

# c) Print all keys
for i in userInfo:
    print('Key:', i)

# ✅ 4. values() METHOD
print('----- values() Method -----')
user_info_values = userInfo.values()
print(user_info_values)  # Output: dict_values([...])

# ✅ 5. keys() METHOD
print('----- keys() Method -----')
user_info_keys = userInfo.keys()
print(user_info_keys)  # Output: dict_keys([...])

# ✅ 6. items() METHOD
print('----- items() Method -----')
dict_items = userInfo.items()
print(dict_items)             # Output: dict_items([...])
print(type(dict_items))       # Output: <class 'dict_items'>

# Looping using items() method
for key, value in userInfo.items():
    print(f'Key is: {key} and Value is: {value}')

# You can use any variable names, not just 'key' and 'value':
# Example:
# for i, j in userInfo.items():
#     print(f'Key: {i}, Value:{j}')
