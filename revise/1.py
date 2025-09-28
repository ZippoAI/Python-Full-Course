import random

# first we need a random number - randint(1, 11) will actually give us 1–10
random_number = random.randint(1, 11)

# guessing games always need to keep looping until the right answer is given
# so while True is the best option
while True:
    # ask the user for a guess each time the loop runs
    # put it inside the loop so if they’re wrong it asks again also make sure the input is an Integer Input
    guess = int(input('Enter a number between 1-10: '))
    
    # check if they got it right
    if guess == random_number:
        print('You won')
        # break is super important here otherwise it will just keep asking forever
        break
    else:
        # don’t break here though cause if they’re wrong you want them to try again
        print('Try Again')

j ikj