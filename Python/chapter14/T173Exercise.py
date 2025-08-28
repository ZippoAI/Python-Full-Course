import time
from functools import wraps
def calculate_time(any_func):
    @wraps(any_func)
    def wrapper_func(*args, **kwargs):
        print(f"Executing: {any_func.__name__}")
        starttime = time.time()
        returned = any_func(*args, **kwargs)
        endtime = time.time()
        print('total time: ', endtime-starttime)
        return returned
    return wrapper_func

@calculate_time
def square_finder(n):
    return [i**2 for i in range(1,n+1)]

square_finder(100000000)