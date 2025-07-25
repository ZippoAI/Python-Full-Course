nums = [1,2,3,4]

def to_power (num, *args):
    if args:
        return [i**num for i in args]
    else:
        return 'You did not pass any args'
    
print(to_power(2, *nums))