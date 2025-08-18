# Decorators - Enhance the functionality of other function

# @ use for decorator 

def decorator_func(any_func):
    def wrapper_func():
        print('This is awesome Function')
        any_func()
    return wrapper_func
    

#This is awesome function 1

def func1():
    print('This is function 1')
    



# This is awesome function 2
@decorator_func #using @ will make sure whenever we call func2 the decorator_func will execute first then func2
def func2():
    print('This is function 2')


func1 = decorator_func(func1)
func1()


# Shortcut using @
func2()