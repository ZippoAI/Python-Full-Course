def even(num):
    for i in range(1,num+1):
        if i%2 == 0:
            yield i

even_numbers = even(10)

for number in even_numbers:
    print(number, end=' ')
