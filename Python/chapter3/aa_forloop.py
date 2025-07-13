'''
name =input(": ")

total = 0
temp_var = ''
for i in range(0, len(name)):
    if name[i] not in temp_var:
        d = name.count(name[i])
        print(f'{name[i]}-{d}')
        temp_var+=name[i]
    i+=1   
'''


'''for i in range(1,11):
    
    if i ==5:
        continue
    print(i)
    i+=1'''


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