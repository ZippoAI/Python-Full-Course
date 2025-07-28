def multiply_ (nums, *args):
    total = 1
    for i in args:
        total*=i
    return total

print(multiply_(2,3,4))


m