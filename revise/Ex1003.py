list_a = [1,2,3,4,5]

list_b = [2,5,1,6,7]
def common_finder(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    print(output)


common_finder(list_a, list_b)