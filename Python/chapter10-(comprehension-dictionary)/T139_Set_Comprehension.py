# Set Comprehension Intro


s = {k*2 for k in range(1,11)}
print(s)


fruits = ['apple', 'kiwi', 'banana', 'orange']

first_character = {i[0] for i in fruits}


print(first_character)