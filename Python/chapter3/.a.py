number = input('Enter a number: ')

total = 0
i = 0

while i < len(number):
    print(f"{total} + {number[i]} = {total+int(number[i])}")
    total+=int(number[i])
    i+=1

n = int(input('Enter a number: '))

total = 0
i = 1

while i<=n:
    print(f'{total} + {i} = {total+i}')
    total+=i
    i+=1