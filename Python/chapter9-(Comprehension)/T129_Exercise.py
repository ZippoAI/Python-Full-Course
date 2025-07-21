l =  ['tac : 1', 'elppa : 2', 'ognam : 3']

numbers = ['123', '456', '789']

reverse_list = [ sublist[::-1] for sublist in l]
print(reverse_list)

empty = []
for i in numbers[::-1]:
   empty.append(i[::-1])
print(empty)


