# ===============================
# 📘 Topic: get() Method and Duplicate Keys in Dictionaries
# ===============================

# ---------------------------------------
# 🔹 get() Method with Default Values
# ---------------------------------------

# ✅ Creating a dictionary
user = {'name': 'Zippo', 'age': 21}

# ⚠️ Key 'ages' does not exist → returns None (doesn't raise error)
print(user.get('ages'))  
# Output: None

# ✅ Providing a default return value if key not found
print(user.get('ages', 'not found !'))  
# Output: not found !

# ---------------------------------------
# 🔹 Behavior with Duplicate Keys
# ---------------------------------------

# ⚠️ If a key is repeated, the last value will override the previous one
user2 = {'name': 'Zippo', 'age': 21, 'age': 24}

print(user2.get('age'))  
# Output: 24 (overrides 21)
