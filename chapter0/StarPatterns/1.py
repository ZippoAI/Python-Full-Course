''' 
Q1- Print this pattern

* * * * * 
* * * * *
* * * * *
* * * * *
* * * * *

'''


for i in range(5):
    for j in range(5):
        print('*', end=' ')
    print()



print('-----------Q2-----------')

''' 
Q2- Print this pattern

*
* *
* * *
* * * *
* * * * *
'''
for i in range(6):
    print(i*" * ")

print('second method: ')
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=' ')
    print()


print('-----------Q3-----------')
''' 
Q3- Print this pattern

* * * * *
* * * *
* * *
* *
*

'''

r = 5
for i in range(1,6):
    for j in range(1,r+1):
        print('*', end=' ')
    r -=1
    print()

print('Method2: ')
r2 = 5
for i in range(r2, 0, -1):
    for i in range(i):
        print('*', end=' ')
    print()


print('-----------Q4-----------')
''' 
Q4- Print this pattern

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''

n = 5

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()



print('-----------Q4-----------')
''' 
Q4- Print this pattern

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

'''

n = 5

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()
    
print('Method2: ')

for i in range(1,6):
    for j in range(1,n+1):
        print(j, end=' ')
    n-=1
    print()