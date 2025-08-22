# Decorators - Enhance the functionality of other function

# @ use for decorator 

def decorator_func(any_func):
    def wrapper_func(*args, **kwargs):
        print('This is awesome Function')
        return any_func(*args, **kwargs)
    return wrapper_func
@decorator_func    
def func(a):
    print('This is function with argument: ',a)

func(8)

@decorator_func
def square(a,b):
    return a+b

print(square(2,3))