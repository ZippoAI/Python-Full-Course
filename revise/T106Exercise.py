print(type(list))

new_list = [1,2,3, [1,2], [3,4],[12]]

empty = []
counter = 0
for i in new_list:
    if type(i) == list:
        counter+=1
print(f"Total list inside list: {counter}")

    
