#Set Data type

# Set is a unordered collection of unique items

s = {1,2,3,4,22,2}
print(s)





# remove dublicate: 

# l = [5,1,1,2,2,3,4,5,4]
# s2 = set(l)

# print(list(dict.fromkeys(l)))

# print(list(set(l)))


# to add eliment in set we use add method
s.add(5)

print(s)

# to remove a item from set we use remove method

s.remove(22)
print(s)



# to clear a set
s.clear()

print(s)

# to copy a set

s1 = {1,2,3,4,22,2}
s2 = s1.copy()

print(s2)

set_ = {1,1.1,2.3, 'string'}

print(set_)