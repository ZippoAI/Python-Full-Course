name = input("Enter your name: ")
zippo = ""
for i in range (0, len(name)):
    if name[i] not in zippo:
        print(f"{name[i]}: {name.count(name[i])} ")
        zippo = zippo + name[i]