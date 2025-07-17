def greater(a,b):
    if a>b:
        return a
    else:
        return b
    
def greatest(x,y,z):
    great = greater(x,y)
    greatest2 = greater(great,z)
    return greatest2


a, b, c = 1,2,4
print(greatest(a,b,c))


def greatestz(a,b,c):
    return max(a,b,c)

a , b, c = map(int,input(": ").split(" "))
print(greatestz(a,b,c))