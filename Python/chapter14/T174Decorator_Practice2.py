from functools import wraps

def only_int(any_func):
    @wraps(any_func)
    def wrapper_func(*args, **kwargs):
        data_types = []
        for arg in args:
            data_types.append(type(arg)==int)
        if all(data_types):
            return any_func(*args, **kwargs)
        else:
            print('Invalid Arguments')
    return wrapper_func




@only_int
def add_all(*args):
    total = 0
    for i in args:
        total+=i
    return total


print(add_all(1,2,3,4,5))