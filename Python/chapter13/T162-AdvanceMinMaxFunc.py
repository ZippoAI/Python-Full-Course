# Advance Min Max Function

numbers = [1,2,3,4,5]

print(max(numbers))

names = ['Zippo', 'Alkama', 'bulbul', 'AB', 'a']

def highest_length(item):
    return len(item)


print(max(names, key= highest_length))
print(max(names, key= lambda a: len(a))) #Both are same

print('-------------------------------')


students = {
    'ZiPPO': {'Score': 100, 'Age': 21},
    'Alkama': {'Score': 78, 'Age': 22},
    'Bulbul': {'Score': 85, 'Age': 20},
    'Elon': {'Score': 95, 'Age': 23}
}

print(max(students, key = lambda a : students[a]['Score']))

students_list = [
    {'Name': 'ZiPPO', 'Score': 90, 'Age': 21},
    {'Name': 'Alkama', 'Score': 78, 'Age': 22},
    {'Name': 'Bulbul', 'Score': 85, 'Age': 20},
    {'Name': 'Elon', 'Score': 95, 'Age': 23}
]

def func(item):
    return item.get('Score')
    
    
print(max(students_list, key = func)['Name'])