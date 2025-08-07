'''
1. Longest Word in a Sentence
Write a program that takes a sentence and finds the longest word in it.

'''
sentence = "Learning Python is both fun and rewarding"
print(max(sentence.split(), key = lambda a:len(a)))


'''
2. Student with Lowest Age
From the students_list given below, find the name of the youngest student.

'''
students_list = [
    {'Name': 'ZiPPO', 'Score': 90, 'Age': 21},
    {'Name': 'Alkama', 'Score': 78, 'Age': 22},
    {'Name': 'Bulbul', 'Score': 85, 'Age': 20},
    {'Name': 'Elon', 'Score': 95, 'Age': 23},
]

print(min(students_list, key = lambda a: a['Age'])['Name'])

'''
3. Product with Highest Price
Given a list of products, find the product with the maximum price.

'''

products = [
    {'name': 'Laptop', 'price': 75000},
    {'name': 'Phone', 'price': 55000},
    {'name': 'Monitor', 'price': 15000},
    {'name': 'Tablet', 'price': 30000}
]

print(max(products, key = lambda a: a['price'])['name'])

'''
4. Find the Shortest Name
Given a list of names, find the one with the fewest characters.

'''
names = ['Abigail', 'Zoe', 'Alex', 'Benjamin', 'Jo']

print(min(names, key = lambda a: len(a)))

'''
5. Country with Longest Capital Name
You're given a dictionary of countries with their capital cities. Find the country whose capital has the longest

'''
capitals = {
    'India': 'New Delhi',
    'USA': 'Washington DC',
    'UK': 'London',
    'Germany': 'Berlin',
    'Argentina': 'Buenos Aires'
}

def func(i):
    return len(capitals[i])

print(max(capitals, key = func))
