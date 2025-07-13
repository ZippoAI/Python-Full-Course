list_a = ['123', '456', '789']


def reverse_l(l):
    empty = []
    for i in l:
        empty.append(i[::-1])
    empty.reverse()
    return empty

print(reverse_l(list_a))

empty2 = []
for i in list_a:
    empty2.append(i[::-1])
print(empty2)
    