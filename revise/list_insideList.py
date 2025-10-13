text2 = [[1,2,3], [4,5,6]]
empty_list = []

for i in text2:
    reverse= i[::-1]
    empty_list.append(reverse)
print(empty_list[::-1])

print("-------------------")    

text = [[1,2,3], [4,5,6]]    
reverse_text = text[::-1]

for i in text[::-1]:
    print(i[::-1], end=" ")



print("----------END----------------")

text3 = [[1,2,3], [4,5,6]]  
empty_list = []
for sublist in text3:
    for i in sublist:
        empty_list.append(i)
print(empty_list[::-1])
        
        
