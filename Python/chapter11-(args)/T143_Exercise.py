def to_power(nums, *args): 
    if args:
        return [i**nums for i in args ]    
    else:
        return 'You did not pass anything'
nums = [1,3,4]
print(to_power(2,*nums))