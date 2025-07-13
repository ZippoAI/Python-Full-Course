# user_input = input("Please enter your name: ")
# user_cha = input("Please enter the character that you want to find: ")

# name = user_input.lower()
# character = user_cha.lower()

# if character in name:
#     print(f"{character} is available in {name}")
# else:
#     print(f"{character} is not available")



















name = input("Enter your name: ")
cha = input("Enter a character: ")

if cha.lower() in name.lower():
    print(f"'{cha}' is in name")
else:
    print("Not available")













