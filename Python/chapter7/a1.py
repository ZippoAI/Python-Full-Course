new_dictionary = {
    'name':'Bulbul',
    'age': '21',
    'Fav_movies':['Avengers', 'Plastic-Man', 'Cat-Man', 'Makdi-Man'],
    'Fav_singers':['Justin Fiber', 'Sawan Mendis', 'Marlie Puth']
}




if ['Avengers', 'Plastic-Man', 'Cat-Man', 'Makdi-Man'] in new_dictionary.values():
    print('Present')
else:
    print('Not present')


print('-----------Loops-----------------')


for i in new_dictionary:
    print(new_dictionary[i])

print('------------')

user_info_values = new_dictionary.values()

print(user_info_values)

