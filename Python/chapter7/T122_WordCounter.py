# Word Counter


# d = {
#     'a':3
# }

print('----------Using Dictionary------------')
name = 'zippo'
def word_counter(n):
    temp = {}
    for i in n:
        temp[i] = n.count(i)
    return temp

print(word_counter(name))




print('------------Using List-------------')
name = 'zippo'
def word_counter_list(n):
    temp = []
    for i in n:
        if i not in temp:
            temp.append(i)
            temp.append(n.count(i))
    return temp
    


print(word_counter_list(name))
