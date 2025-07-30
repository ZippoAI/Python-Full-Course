# Filter Function 


def is_even(a):
    return a%2 == 0

numbers = [3,2,1,4,5,6,7,5,4]

evens = list(filter(is_even, numbers))

evens2 = list(filter(lambda a: a%2==0, numbers)) #Using Lambda

print(evens)
print(evens2)

new_evens = [i for i in numbers if i%2 == 0] #using list comprehension

print(new_evens)