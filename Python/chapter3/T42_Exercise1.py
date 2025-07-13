import random

winning_number = 5

number = int(input("Enter a number : "))

if number == winning_number:
    print("You won")
else:
    if number>winning_number:
        print("Too high")
    else:
        print("Too low")
