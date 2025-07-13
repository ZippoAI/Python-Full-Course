name, cha= input("Enter your name and a character comma separeted: ").split(",")



print(f"Your name is- {name.replace(" " , "")} and lenght is {len(name.replace(" " , ""))} \nCharacter count is {name.lower().count(cha.replace(" " , "").lower())} ")