name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))

if name.startswith("a") or age == 18:
    print(f"Hello, {name} and your age is {age}")

else:
    print(f"Your name should start with letter A and your age should be above 18 to play this game!")
