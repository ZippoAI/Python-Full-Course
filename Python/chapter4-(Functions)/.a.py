import random

# winning_number = random.randint(1,50)
winning_number = 30

start = input("Do you want a minimum attempt to complete this game? Y/N: ")

if start.lower().startswith("y"):
    attempting = int(input("Enter a number of attempt you want: "))
    for attem in range(1,attempting+1):

        number = int(input(f"attemps : {attem} | Enter a number between 1 to 50: "))
        if number == winning_number:
            print(f"You won and you guessed it in {attem} times")
            break
        else:
            if winning_number<number:
                print("Too High")
            else:
                print('Too low')
        if attem == attempting:
            print(f"Game Over! As you have crossed {attempting} attempts so no attempt left")





if start.lower().startswith("n"):
   
    guess = 1
    while winning_number:
        number1 = int(input(f"attemps : {guess} | Enter a number between 1 to 50: "))
        
        if number1>winning_number:
                
                print("Too High")
                # number1 = int(input(f"attemps : {guess} | guess again:  "))
        else:
                print("Too Low")
                # number1 = int(input(f"attemps : {guess} | guess again:  "))
        
        if number1 == winning_number:
            print(f"You won and you guessed it in {guess} times")
            break
        guess += 1
            
        
