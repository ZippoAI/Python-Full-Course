# 1. Capitalize Names
names = ["ziPpo", "bUlBul", "jUstin", "fiBEr"]

result_name = list(map(lambda a: a.capitalize(), names))
print(result_name)


# 2. Square Numbers

nums = [1, 2, 3, 4, 5]

nums_result = list(map(lambda a: a**2, nums))
print(nums_result)

# 3. Convert Strings to Integers

str_nums = ["10", "20", "30", "40"]

str_result = list(map(lambda a: int(a), str_nums))
print(str_result)

# 4. Add 5 to Each Element

numbers = [10, 15, 20, 25]

numbers_result = list(map(lambda a: a+5, numbers))
print(numbers_result)


# 5. Filter and Double Even Numbers (a little tricky)
values = [1, 2, 3, 4, 5, 6]

def even_check(l):
    empty = 0
    if l%2==0:
        empty = (l*2)
    else:
        empty = ('X')
    return empty
        
result3 = list(map(even_check, values))
print(result3)
    
