

def decorator_func(any_func):
    def wrapper_func():
        print('This is awesome function')
        any_func()
    return wrapper_func

def func1():
    print('This is function 1')

@decorator_func
def func2():
    print('This is function 2')



# f = decorator_func(func1)
# f()


func2()