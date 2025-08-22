from functools import wraps
def print_function_data(any_function):
    @wraps(any_function)
    def print_func(*args, **kwargs):
        print(f'You are calling: {any_function.__name__} function' )
        print(any_function.__doc__)
        return any_function(*args, **kwargs)
    return print_func 




@print_function_data
def add(a,b):
    '''
    This function takes two numbers as arguments and return their sum
    '''

    return a+b

print(add(4,5))

print('---------------------')

@print_function_data
def multiply(a,b):
    '''
    This function takes two input and return their multiply value
    '''
    return a*b

print(multiply(5,5))

