list_a = [1,2,3,4,5]

list_b = ['apple1' , 'apple2', 'apple3']


def list_reverse(reverse):
    rever = []
    while reverse:
        rev = reverse.pop()
        rever.append(rev)
    return rever

print(list_reverse(list_b))


# def reverse_li(l):
#     l.reverse()
#     return l
# print(reverse_li(list_b))