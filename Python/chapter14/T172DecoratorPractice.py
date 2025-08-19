from functools import wraps

# @print function data

def print_func_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"You are calling {function.__name__} function")
        print(f"{function.__doc__}")
        return function(*args, **kwargs)
    return wrapper

@print_func_data
def addition(a,b):
    '''
    This Function takes two numbers and return their sum
    '''
    return a+b

print(addition(4,5))