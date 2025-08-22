
def decorator_func(any_func):
    def wrapper_func():
        print('This is wrapper Function')
        any_func()
    return wrapper_func


@decorator_func
def func1():
    print('This is function 1')

func1()




def func2():
    print('This is function 2')

var = decorator_func(func2)
var()