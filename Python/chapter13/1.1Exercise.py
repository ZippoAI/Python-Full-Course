nums = [1, 2, 3, 4, 5, 6]


new_l1 = list(map(lambda a: a**2, nums))

print(new_l1)



celsius = [0, 10, 20, 34.5]

fahrenheit = list(map(lambda a: (a * 9/5) + 32 ,celsius))

print(fahrenheit)

names = ["Alice", "Bob", "Charlotte", "David", "Eleanor"]

new_name = list(filter(lambda a: len(a)> 5, names))
print(new_name)


nums = [-5, 3, -1, 101, 0, 8]

new_num = list(map(lambda a: a*2 , filter( lambda a: a>0, nums)))

print(new_num)


items = ["12", "abc", "45", "hello", "90"]
remove_non_digit = list(map(lambda a: int(a), filter(lambda a: a.isdigit(), items)))
print(remove_non_digit)

