l1 = [1,2,3]

l2 = [4,5,6]

l3 = [7,8,9]

def func(*args):
    empty = []  
    for i in args:
        empty.append(sum(i)/len(i))
    return empty
        
    

print(func(l1,l2,l3))