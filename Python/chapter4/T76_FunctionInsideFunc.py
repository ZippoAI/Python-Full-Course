def great(a,b):
    if a>b:
        return a
    else:
        return b
    
def greatest(a,b,c):
    greater = great(a,b)
    return great(greater,c)

a = int(input("1st: "))
b = int(input("2nd: "))
c = int(input("3rd: "))

great2 = greatest(a,b,c)

print(great2)