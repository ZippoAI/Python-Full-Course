def num_string(n):
    numstring = [str(i) for i in n if type(i) == int or type(i) == float]
    return numstring

input_value = [True, False, 'zippo', [1,2,3], 1, 1.0, 3]
print(num_string(input_value))



