matrix = [[1,2,3], [4,5,6], [7,8,9]] #2d List(because 2 list----> list inside list)
# 3 items ---> 3 List
i = 0
for sub in matrix:
    for i in sub:
        print(i, end=" ")
#     # i+=1
print("\n-----------------")

print(type(matrix))

print('-----------')


print(matrix[2][0])

