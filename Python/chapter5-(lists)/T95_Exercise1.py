'''Define a function which will take list containing number as input and return list containing square of every elements'''



def square(number):
    empty = []
    for i in number:
        empty.append(i*i)
    return empty

num1 = int(input('First: '))
num2 = int(input('Second: '))

number = list(range(num1,num2+1))

print(square(number))