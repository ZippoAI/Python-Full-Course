def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count+=1
    return count

number = [1,2,3, [1,2,3], [1,2,3], 4,4,4,[6,6]]

print(sublist_counter(number))