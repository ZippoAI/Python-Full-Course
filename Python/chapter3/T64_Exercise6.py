winning = 43

guess = 1

number = int(input("Guess a number between 1 to 100: "))
game_over = False

while not game_over:
    if number == winning:
        print(f"You win, and you guessed this number in {guess} times ")
        game_over = True

        #win
    else:
        if  number < winning:
            print("Too low")
            guess = guess + 1
            number = int(input("Guess Again: "))
        else:
            print("Too high")
            guess = guess + 1
            number = int(input("Guess Again: "))




winning_number = 15

total_guess = 5

guess_count = 1

number = int(input("Guess a number between 1 to 20 You have 5 Total Guess: "))

while True:
    if number == winning_number:
        print(f'You won and you guessed this in {guess_count} times')
        break
    
    elif total_guess == guess_count:
        print('No guess Left You LOST')
        break
    
    elif number>winning_number:
        print('Too high and left guess:', total_guess-guess_count)
           
    elif  number<winning_number:
        print('Too low left guess:', total_guess-guess_count)
        
        
    guess_count+=1

    number = int(input("Wrong guess, guess again between 1 to 20: "))