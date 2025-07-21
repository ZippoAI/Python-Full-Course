# for i in range(1,12):
#     print(i**2)

squared = [ i for i in range(10,0,-1)]

print(squared)


names= ['zippo', 'bulbul', 'alkama']


# list comprehension solution 1.1
first_character = [char[0] for char in names]

print(first_character)

# Normal solution 1.1
# def first_character(n):
#     empty_list = []

#     for i in n:
#         empty_list.append(i[0][0])
#     return empty_list

# print(first_character(names))

empty_list = []
for i in names[0]:
    
    print(i, end="")