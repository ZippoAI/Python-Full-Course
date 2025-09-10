# List vs Generator
# Memory usage, Time
# When to use list, when to use generator
import time

# starttime = time.time()
# l = [i**2 for i in range(100000000)] 
# endtime = time.time()
# print(endtime-starttime)


starttime2 = time.time()
g = (i**2 for i in range(100000000)) 
for i in g:
    pass
endtime2 = time.time()
print(endtime2-starttime2)