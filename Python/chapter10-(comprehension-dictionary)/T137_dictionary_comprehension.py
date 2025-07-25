# Dictionary Comprehension 

# Ouput = {1:1 , 2:4, 3:9}

square = {value:value**2 for value in range(1,4)}

print(square)


name = 'ZIPPO'
character_count = {i:name.count(i) for i in name}
print(character_count)


# final_output = {}
# for i in (name):
#     final_output[i] = name.count(i)

# print(final_output)