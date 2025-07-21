def cube_finder(n):
    empty = {}
    for i in range(1, n+1):
        empty[i] = i * i * i   # store cube as value
    return empty

print(cube_finder(3))
