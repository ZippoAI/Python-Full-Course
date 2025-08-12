# Pass a function as an argument


def square(a):
    return a**2


l2= [1,2,3,4,5]

def func(func, l):
    new_l = [func(i) for i in l]
    return new_l

print(func(square, l2))

  