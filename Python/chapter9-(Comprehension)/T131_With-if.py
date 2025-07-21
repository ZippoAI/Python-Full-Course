# List Comprehension with if statement



numbers = list(range(1,11))


even_nums = [i for i in numbers if i%2 == 0 ]


print(even_nums)

odd_nums = [i for i in range(1,11) if i%2==1]
print(odd_nums)

