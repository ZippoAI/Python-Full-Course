names = ["Alice", "bob", "Angela", "Mike", "adam", "Brian"]

def func(l):
    return l[0] == 'a' or l[0] == 'A'

result = list(filter(func, names))
print(result)

result2 = list(filter(lambda a: a[0].lower() == 'a' , names))

print(result2)