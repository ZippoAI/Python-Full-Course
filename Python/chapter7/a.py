new_dictionary = dict(name='Zippo', age = 21)

print(new_dictionary)

#FromKey



d = {'name':'ZiPPO', 'age':'unknown'}


# d = dict.fromkeys(['name', 'age'], ['unknown', 'unkown'])

# print(d)


print(d.get('name'))


print(d.get('name'))

if d.get('name'):
    print('Present')
else:
    print('Not Present')

d2 = d.copy()

d2.popitem()
print(d)