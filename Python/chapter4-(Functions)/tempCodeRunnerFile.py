x = 5 # Global Variable
def func():
    global x
    x = 7 #local variable
    return x

print(x)