square = [i**2 for i in range(1,11)]

print(square)


square_generator = (i**2 for i in range(1,11)) # instead of [] ---> ()
print(square_generator)

for num in square_generator:
    
    print(num)

print('---------------')

for num in square_generator:

    print(num)