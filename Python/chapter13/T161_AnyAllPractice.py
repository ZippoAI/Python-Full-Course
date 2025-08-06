def my_sum (*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        result = 0
        for num in args:
            result+=num
        return result
    else:
        return 'Wrong Input'
    



l1 = [1,2,3,4]
l2 = [4,5,6,7]

print(my_sum(1,2,3,4,6.9))