# List comprehension with if else:


nums = [1,2,4,5,6,7,8,9,10]

new_list = [i*2 if i%2 == 0 else -i for i in nums]

print(new_list)