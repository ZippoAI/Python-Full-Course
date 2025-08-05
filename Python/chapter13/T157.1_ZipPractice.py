# 1- Add corresponding elements of two lists:

l1 = [1, 2, 3]
l2 = [4, 5, 6]
# Output: [5, 7, 9]

corresponding_output = []

for pair in zip(l1,l2):
    corresponding_output.append(sum(pair))
print(corresponding_output)

# 2- Create a dictionary from two lists:
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

dictionary_output = dict(zip(keys, values))
print(dictionary_output)

# 3- Find pairwise maximum between two lists:
l_1 = [4, 8, 2]
l_2 = [3, 10, 5]
# Output: [4, 10, 5]

pairwise_output = [max(pair) for pair in zip(l_1, l_2)]
print(pairwise_output)


# 4 - Check if elements in two lists are equal:
equal_l1 = [1, 2, 3]
equal_l2 = [1, 0, 3]
# Output: [True, False, True]

equal_elements = [True if a==b else False for a,b in zip(equal_l1, equal_l2)]
print(equal_elements)


# 5 - Combine names and scores into tuples:
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]
# Output: [('Alice', 85), ('Bob', 90), ('Charlie', 78)]


Combine_names = list(zip(names, scores))
print(Combine_names)

# 6- Multiply corresponding elements of two lists:
Multiply_l1 = [1, 2, 3]
Multiply_l2 = [4, 5, 6]
# Output: [4, 10, 18]

Multiply_corresponding = [a*b for a,b in zip(Multiply_l1, Multiply_l2)]
print(Multiply_corresponding)

# 7- Count how many elements are equal in two lists:
Count_a = [1, 2, 3, 4]
Count_b = [1, 0, 3, 5]
# Output: 2 (since 1 and 3 match)

count = 0
op = []
for a , b in zip(Count_a, Count_b):
    if a == b:
        count+=1
        op.append(f"{a} == {b}")

print("Output: ", count, "Because -", ", ".join(op))


# 8 - Swap elements of tuples from zip:
swap_l1 = ['a', 'b']
swap_l2 = [1, 2]
# Output: [(1, 'a'), (2, 'b')]

swap_list = zip(swap_l2,swap_l1)

swap_l1, swap_l2 = zip(*swap_list)
new_list = list(zip(swap_l1,swap_l2))
print(new_list)

# 9 - Find index where elements are different in two lists:
index_a = [5, 6, 7, 8]
index_b = [5, 0, 7, 9]
# Output: [1, 3]
same_index_output = []
different_index_output = []
for a,b in zip(index_a, index_b):
    if a !=b :
        same_index_output.append(index_a.index(a))
    else:
        different_index_output.append(index_a.index(a))
print("same: " ,same_index_output)
print("Different: " , different_index_output)

# 10 - Print full names by combining first and last names:
first = ['John', 'Jane']
last = ['Doe', 'Smith']
# Output: ['John Doe', 'Jane Smith']

new_full = list(zip(first, last)) 
full_name= []
for i, b in new_full:
    full_name.append(i+ ' ' +b)
print(full_name)
    


