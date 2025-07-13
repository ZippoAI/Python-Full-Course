# ===============================
# 📘 Topic: Dictionary Methods in Python
# ===============================

# ---------------------------------------
# 🔹 fromkeys() Method
# ---------------------------------------

# ✅ Create a dictionary using a list of keys, all having the same value
d = dict.fromkeys(['name', 'age', 'height'], 'unknown')
print(d)  
# Output: {'name': 'unknown', 'age': 'unknown', 'height': 'unknown'}

# ✅ Using a tuple instead of a list
f = dict.fromkeys(('name', 'age', 'height'), 'unknown')
print(f)
# Output: {'name': 'unknown', 'age': 'unknown', 'height': 'unknown'}

# ⚠️ Using a list as a value - all keys will point to the same list
g = dict.fromkeys(['name', 'age', 'height'], ['unknown', 'unknown'])
print(g)
# Output: {'name': ['unknown', 'unknown'], 'age': ['unknown', 'unknown'], 'height': ['unknown', 'unknown']}

# ---------------------------------------
# 🔹 get() Method
# ---------------------------------------

# ✅ Creating a simple dictionary
d = {'name': 'unknown', 'age': 'unknown'}

# ❌ Accessing a non-existent key directly will throw an error
# print(d['names'])  # Uncommenting this line will raise KeyError

# ✅ Using get() prevents errors, returns None if key is not found
print(d.get('names'))  # Output: None

# ✅ Example usage in a conditional
if d.get('name'):
    print('present')
else:
    print('not present')
# Output: present

# ---------------------------------------
# 🔹 copy() and clear() Methods
# ---------------------------------------

# ✅ Copying a dictionary
d1 = d.copy()

# ✅ Clearing the original dictionary
d.clear()

print(d)   # Output: {}
print(d1)  # Output: {'name': 'unknown', 'age': 'unknown'}
