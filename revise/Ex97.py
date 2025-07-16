numbers = [1,2,3,4,5]
def rev_list(l):
    empty_l = []
    copy = l.copy()
    while copy:
        empty_l.append(copy.pop())
    return empty_l

print(rev_list(numbers))

# def rev_list(l):
#     r_list = []
#     copy = l.copy()
#     while copy:
#         r_list.append(copy.pop())
#     return r_list
# print(rev_list(numbers))