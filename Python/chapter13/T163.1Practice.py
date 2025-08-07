'''
✅ Question 1: Sort strings by length
You are given a list of fruits:

'''
fruits = ['Watermelon', 'Fig', 'Pineapple', 'Kiwi']


print(sorted(fruits , key=len,))
print(sorted(fruits , key=len, reverse=True))

'''
✅ Question 2: Sort a tuple of numbers in descending order
You have a tuple
'''

numbers = (4, 1, 6, 3, 8)

print(sorted(numbers, reverse=True))

'''
✅ Question 3: Sort a set of names alphabetically (case insensitive)
You are given a set of names:

'''

names = {'Alice', 'bob', 'charlie', 'David'}

print(sorted(names, key=str.lower))

'''
✅ Question 4: Sort a list of student dictionaries by their score
You have a list:
'''

students = [
    {'name': 'John', 'score': 88},
    {'name': 'Emma', 'score': 92},
    {'name': 'Kelly', 'score': 75}
]

print(sorted(students, key= lambda a: a['score']))
print(sorted(students, key= lambda a: a['score'], reverse=True))

'''
✅ Question 5: Sort words in a sentence by alphabetical order
You are given a sentence:

'''
sentence = "Python is a powerful programming language"

words = sentence.split()

print(sorted(words, key=str.lower))