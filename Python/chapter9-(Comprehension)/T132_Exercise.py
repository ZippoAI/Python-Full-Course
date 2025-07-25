def int_or_float_finder(l):
    result = [i for i in l if type(i)== int or type(i)== float]
    return  list(result)
inpt  = [1,3,4, True , 'hello', 3.4, 1.0]
print(int_or_float_finder(inpt))


import time

s = time.time()
d = range(11)
empty = []
for i in d:
    empty.append(i)
print(i)

print(time.time() - s)