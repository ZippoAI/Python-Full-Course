number1 = [[41,51,61],[71,81,91]]

empty_list = []

for sublist in number1:
    temp =[]
    for i in sublist:
        rev1 = str(i)[::-1]
        temp.append(int(rev1))
    empty_list.append(temp)
print(empty_list)


print("-----------------------")



number2 = [41,51,61]
temp2 = []
for i in number2:
    rev2 = str(i)[::-1]
    temp2.append(int(rev2))
print(temp2)



print("-----------------------")


number3 = [12345]

for i in number3:
    rev3 = int(str(i)[::-1])
    print(rev3)


print("-----------------------")


number5 = [[41,51,61],[71,81,91]]
empty_l = []
for sublist in number5:
    temp= []
    for i in sublist:
        rev4 = int(str(i)[::-1])
        temp.append(rev4)
    empty_l.append(temp)
print(empty_l)
    