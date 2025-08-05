# Q: Define a function that will take any no of list containing number adn return average
l1 = [1,2,3]

l2 = [4,5,6]

l3 = [7,8,9]

def average_finder(*args):
    empty = []
    for pair in zip(*args):
        empty.append(sum(pair)/len(pair))
    return empty

print(average_finder(l1,l2,l3))


        
def average_finder2(*args):
    average = [(sum(pair))/len(pair) for pair in zip(*args)]
    return average

print(average_finder2(l1,l2,l3))

# using lambda:

average_finder3 = lambda *args : (sum(pair)/len(pair) for pair in zip(*args))

print(list(average_finder3(l1,l2,l3)))