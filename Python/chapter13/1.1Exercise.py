l1 = [1,2,3,4]
l2 = [4,3,2,1]
l3 = [5,4,1,3]

def average_finder_column(*args):
    result = []
    for pair in zip(*args):
        result.append(sum(pair)/len(pair))
    return result

print(average_finder_column(l1,l2,l3))

def average_finder_row(*args):
    result = []
    for i in args:
        result.append(sum(i)/len(i))
    return result
    
print(average_finder_row(l1,l2,l3))