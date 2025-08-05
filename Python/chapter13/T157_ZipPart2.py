l1 = [1,2,3,4,5,7]
l2 = [4,2,1,4,5,9]

new_l = list(zip(l1, l2))



print(new_l)

combined = [(1, 4), (2, 2), (3, 1), (4, 4), (5, 5), (7, 9)]

l3, l4 = zip(* new_l)

print(l3)
print(l4)


print('----------------')

greater = []

for pair in zip(l1,l2):
    greater.append(max(pair))
print(greater)

# same code without max()

greater2 = []
i = 0
for a, b in zip(l1,l2):
    if a>b:
        greater2.append(a)

    else:
        greater2.append(b)
print(greater2)




