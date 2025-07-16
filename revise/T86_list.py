numbers = [[12],[13],[14],[15]]
empty = []
for sublist in numbers:
    rev = []
    for i in sublist:
        rev.append(int(str(i)[::-1]))
    empty.append(rev)
print(empty)

    
 