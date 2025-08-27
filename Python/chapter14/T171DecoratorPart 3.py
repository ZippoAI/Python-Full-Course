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
def add(a,b):
    '''
    This is add function
    '''
    return a + b

a = decorator_func(add)

print(a(5,5))