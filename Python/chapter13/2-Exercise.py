def is_even (a):
    return a%2 == 0

numbers = list(range(1,11))

evens= list(filter(is_even, numbers))

print(evens)


def is_even2 (a):
    result = []
    for i in a:
        if i%2==0:
            result.append(i)
    return result

print(is_even2(numbers))