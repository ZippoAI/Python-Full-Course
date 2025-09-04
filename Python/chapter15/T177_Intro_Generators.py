#Generators

#Generators are iterators



l = [1,2,3] #iterable


for i in l:
    print(i)
print('-----------------------')
# how it works: 
i = iter(l)
print(next(i))
print(next(i))
print(next(i))

print('----------------')
print(list(map(lambda a: a*2, l))) # iterator
print('---------------')

for num in map(lambda a: a*2, l):
    print(num)
    


print('--------------')



# memory ------------- [..................]

# memory ----- ()



