matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# ouput: [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_matrix2 = []
final_matrix = [i for j in matrix for i in j]

print(final_matrix)

new_matrix = []
for i in matrix:
    for j in i:
        new_matrix.append(j)
print(new_matrix)
