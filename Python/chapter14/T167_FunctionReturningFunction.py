# Function Returning Function

def outer_func():
    def inner_func():
        print('inside inner func')
    return inner_func()

outer_func()

def outer_func2(msg):
    def inner_func2():
        print(f"message is : ", msg)
    return inner_func2()

outer_func2("Hello")