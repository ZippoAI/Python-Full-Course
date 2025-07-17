
list1 = [1,2,3,4,5]

list2 = [4,54,3,23,12,1]


def find_common(l1,l2):
    emptyL = []
    for i in l2:
        if i in l1:
            emptyL.append(i)
    return emptyL
    

print(find_common(list1,list2))