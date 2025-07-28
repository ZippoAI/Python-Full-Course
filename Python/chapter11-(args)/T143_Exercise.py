def to_power(nums, *args):
    if args:
        return [i**nums for i in args]
    else:
        return "You did not pass anything"


new_list = [1,2,3]
print(to_power(3, *new_list))