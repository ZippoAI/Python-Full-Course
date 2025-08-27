from functools import wraps


def decorator_func(any_func):
    @wraps(any_func)
    def wrapper(*args, **kwargs):
        print(f'You are calling {any_func.__name__} Function')
        print(any_func.__doc__)
        return any_func(*args, **kwargs)
    return wrapper

@decorator_func
def add(a,b):
    '''
    It will take two numbers as argument and returns their sum
    '''
    return a + b

print(add(4,5))
