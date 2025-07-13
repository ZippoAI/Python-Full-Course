name = input("Enter your name: ")

age = int(input("Enter Your age: "))

over = False

while not over:
    if name.lower().startswith("a") and age > 18:
        print("You can enter the website")
    over = True 
    if name[0] !="A" or name[0] !="a" :
        print("Your name should start with letter A")
        name = input("Enter your name again: ")
        age = int(input("Enter Your age: "))
        
    elif age <18:
        print("your age should be 18+")
        age = int(input("Enter Your age again: "))
        name = input("Enter your name: ")

        