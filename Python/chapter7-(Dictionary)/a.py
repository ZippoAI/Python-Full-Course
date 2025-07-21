def square_finder(n):
    empty = {}
    for i in range(1,n+1):
        empty[i] = i*i
    return empty



print(square_finder(4))


def double_finder(n):
    empty = {}
    for i in range(1,n+1):
        empty[i] = i*2
    return empty



print(double_finder(3))



def number_word_finder(n):
    empty = {}
    for i in range(1,n+1):
        empty[i] = f"Number {i}"

    return empty


print(number_word_finder(3))


def reverse_cuber(n):
    empty_cube = {}
    for i in range(1,n+1):
        
        empty_cube[i**3] = i

    return empty_cube

print(reverse_cuber(3))



def even_odd(n):
    empty = {}
    for i in range(1,n+1):
        if i %2 ==0:
            empty[i] = 'Even'
        else:
            empty[i] = 'odd'
    return empty

print(even_odd(4))

