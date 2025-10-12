# Loop-only Spiral Pattern (Clockwise)

n = int(input("Enter n: "))

# Step 1: Create an empty n x n matrix using loops
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    matrix.append(row)

# Step 2: Initialize boundaries
top = 0
bottom = n - 1
left = 0
right = n - 1

num = 1  # number to fill
total = n * n

# Step 3: Fill the spiral using only loops
while num <= total:
    # Traverse from left to right
    for i in range(left, right + 1):
        if num <= total:
            matrix[top][i] = num
            num += 1
    top += 1

    # Traverse from top to bottom
    for i in range(top, bottom + 1):
        if num <= total:
            matrix[i][right] = num
            num += 1
    right -= 1

    # Traverse from right to left
    for i in range(right, left - 1, -1):
        if num <= total:
            matrix[bottom][i] = num
            num += 1
    bottom -= 1

    # Traverse from bottom to top
    for i in range(bottom, top - 1, -1):
        if num <= total:
            matrix[i][left] = num
            num += 1
    left += 1

# Step 4: Print the matrix neatly
for i in range(n):
    for j in range(n):
        # Formatting: print with spaces, no built-in string methods
        if matrix[i][j] < 10:
            print(" ", matrix[i][j], end=" ")
        else:
            print(matrix[i][j], end=" ")
    print()
