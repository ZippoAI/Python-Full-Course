# more about list


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1,2,23,4,5,52,1,2,1,2,1]

find1 = numbers.index(1)
find2 = numbers.index(1, find1 + 1)
find3 = numbers.index(1, find2 + 1)
find4 = numbers.index(1, find3 + 1)
find5 = numbers.index(1, find4 + 1)

print(find5)


numberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def negList(l):
    emptyL = []
    for i in l:
        emptyL.append(-i)
    return emptyL


print(negList(numberlist))
