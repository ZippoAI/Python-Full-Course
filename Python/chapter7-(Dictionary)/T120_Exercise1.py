# Cube finder

def cube_finder(n):
    cubees = {}
    for i in range(1,n+1):
        cubees[i] = i*i
    return cubees

print(cube_finder())