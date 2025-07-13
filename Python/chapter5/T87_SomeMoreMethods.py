fruit= ['orange', 'apple', 'banana', 'kiwi','apple']


print(fruit.count('apple'))


print("--------------------SORTED--------------------------------------")

number = [1,3,4,5,2,6,8,9,7]
print(sorted(number)) #sorted function just only print the data in a sorted order but it doesnt actually sort the numbers.lets take an example
numbers2 = [1,3,4,5,2,6,8,9,7]
sorted(numbers2)
print(numbers2)


print("--------------------SORT--------------------------------------")

#Sort method actually sort the data permanently
numbers1 = [1,3,4,5,2,6,8,9,7]
numbers1.sort()
print(numbers1)


print("------------------------CLEAR----------------------------------")
#Clear method will make our list empty 
number4 = [1,3,4,5,2,6,8,9,7]
number4.clear()
print(number4)

print("----------------------COPY------------------------------------")
#Copy Function copies the data of that list
number5 = [1,3,4,5,2,6,8,9,7]
copy = number5.copy()
print(copy)