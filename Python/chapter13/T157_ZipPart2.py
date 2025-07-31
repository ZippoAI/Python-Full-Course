l1 = [a for a in range(1,11) if a%2 ==0]
l2 = [a for a in range(1,11) if a%2 ==1]


final = list(zip(l2, l1))

print(final)

# list unpack

li1 , li2 = zip(*final)

print("li1 :" , li1)
print("li2 :" ,li2)

l3 = [a for a in range(1,11) if a%2 ==0]
l4 = [a for a in range(1,11) if a%2 ==1]

new_list = []
for i in zip(l3,l4):
    new_list.append(max(i))
print(new_list)


# new_list = []
# for i in range(len(l3)):  
#     if l3[i] > l4[i]:
#         new_list.append(l3[i])
#     else:
#         new_list.append(l4[i])
# print(new_list)


