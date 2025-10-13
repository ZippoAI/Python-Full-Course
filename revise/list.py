fruits = ['mango', 'apple']

fruits.insert(0,'Orange')

print(fruits)


fruits1 = ['Apple', 'kiwi']

fruits2 = ['Orange', 'Kola']

fruits1.extend(fruits2)
print(fruits1)


# Delete Data from list

fruits = ['mango', 'apple', 'Apple', 'kiwi', 'mango']
print()
# fruits.pop()
print(fruits)

fruits.remove('mango')
print()
print(fruits)