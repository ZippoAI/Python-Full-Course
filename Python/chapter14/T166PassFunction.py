# Pass a function as an argument
def three_power(a):
    return a**3

def square(a):
    return a**2

l = [1,2,3,4,5]
  
print(list(map(square, l)))

#instead of using map we can do this too
def map_func(func, a):
    empty = []
    for i in a:
        empty.append(func(i))
    return empty
    
print(map_func(square, l))
print(map_func(lambda a: a**2, l))

# map() and map_func both do the same work