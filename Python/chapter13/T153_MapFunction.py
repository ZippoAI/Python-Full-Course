# map() Function

numbers = [1,2,3,4]

def square(l):
    return (l**2)


print([square(1), square(2), square(3), square(4)])


print()
print('-------Using Map Function---------')
print()

squares = list(map(square, numbers))

print(squares)

print()
print('-------Using Lambda---------')
print()

# we can do this using lambda too
squares2 = list(map(lambda a: a**2, numbers))
print(squares2)

print()
print('-------Using List Comprehension---------')
print()

squares3 = [i**2 for i in numbers]
print(squares3)


print()
print("--------Using normal method--------")
print()
empty = []
for i in numbers:
    empty.append(square(i))
print (empty)


names = ['abc', 'abcd', 'abcde']

length = map(len, names)
for i in length:
    print(i)