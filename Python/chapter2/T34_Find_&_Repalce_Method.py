# Replace() Method
# Find() Method

string = " she  is beautiful and she is good dancer"

# print(string.replace(" ", "_"))
# print(string.replace("is", "was" ))

is_position1= string.find("is") #is pos1 ----->number
is_position2=string.find("is",is_position1+1)
print(is_position2)
print(is_position1)

# Learn the find method properly