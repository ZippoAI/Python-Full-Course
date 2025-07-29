# We use Enumerate function with for loop to strack position of our item in iterable


# how we can do this without the enumerate function
names = ['abc', 'abcdef', 'zippo']

pos = 0
for i in names:
    pos+=1
    print(f"{pos}: {i}")


print('----------------------------')

print()


# With enumerate function 

for pos , name in enumerate(names):
    print(f'{pos} -------> {name}')

print()
print('--------------------')

def find_pos (l, target):
    for pos, name in enumerate(l):
        if name == target:
            return pos
    else:    
        return -1
        

print(find_pos(names, 'zippo'))

print('--------------------')

def find_pos2 (l, target):
    for pos, name in enumerate(l):
        if pos == target:
            return name
    else:    
        return -1
        

print(find_pos2(names, 2))