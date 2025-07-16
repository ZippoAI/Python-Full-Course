# more about list


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1,2,23,4,5,52,1]

find1 = numbers.index(1)

find2 = numbers.index(1, find1 + 1)

print(numbers.index(1, find2 + 1))
