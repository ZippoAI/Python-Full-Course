# Print numbers from 1 to 50. But for multiples of 3, print "Fizz", for multiples of 5 print "Buzz", and for both print "FizzBuzz".

for i in range(1,51):
    if i%5==0 and i%3 == 0:
        print('FizzBuzz ', end="")
    elif i%3==0:
        print('Fizz ',  end="" )
    elif i%5==0:
        print('Buzz ', end="")
    
    else:
        print(i, end=" " )

