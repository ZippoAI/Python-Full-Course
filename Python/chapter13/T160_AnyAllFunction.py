# Any , All Function

numbers1= [2,4,6,8,10]
numbers2= [1,3,5,4,7,9]
evens_one = []
for i in numbers1:
    if i%2==0:
        evens_one.append(True)
        pass
print(evens_one)

result = (all([num%2==0 for num in numbers1]))

print(result)