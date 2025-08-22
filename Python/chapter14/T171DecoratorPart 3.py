from functools import wraps

def decorator_func(any_func):
    @wraps(any_func)
    def wrapper_func(*args, **kwargs):
        '''
        This is Wrapper Function
        '''
        print('This is awesome Function')
        return any_func(*args, **kwargs)
    return wrapper_func
@decorator_func    
def func(a):
    print('This is function with argument: ',a)



@decorator_func
def square(a,b):
    '''This is add function'''
    return a+b

print(square.__doc__)
print(square.__name__)