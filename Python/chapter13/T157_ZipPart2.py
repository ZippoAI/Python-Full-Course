l1 = [a for a in range(1,11) if a%2 ==0]
l2 = [a for a in range(1,11) if a%2 ==1]


final = list(zip(l2, l1))

print(final)

# list extraction

li1 , li2 = zip(*final)

print(li1)
print(li2)