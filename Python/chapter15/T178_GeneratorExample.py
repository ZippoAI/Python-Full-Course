# Create your first generator with generator function

# 1.) Generator Function

def loop(a):
    for i in range(1,a+1):
        print(i) 
    
loop(10)

print('-----------')

def loop2(a):
    for i in range(1,a+1):
        yield(i) 
    
print(loop2(10))

print('---------')

for number in loop2(10):
    print(number)


print('----------------3---------------')

numbers = loop2(10)

for num in numbers:
    print(num)




# memory ----------> 1, 
