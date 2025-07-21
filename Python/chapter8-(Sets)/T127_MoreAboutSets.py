s = {
    'a', 'b', 'c'
}

if 'a' in s:
    print('present')
else:
    print('Not present')


# for i in==========
s1 = {1,2,4,5}

s2 = {3,4,5,6}

print(s1.union(s2))

#We can also do union using | 

s3 = {1,2,4,5}

s4 = {3,4,5,6}

print(s3 | s4)


#Intersection: Finding Common 
s3 = {1,2,4,5}

s4 = {3,4,5,6}

print(s3 & s4)