user = {
    'name':'Zippo',
    'age': 22,
}

print(user['name'])


user1 = dict(name = 'Bulbul', age = 22)

print(user1['name'])

print('-------------')

user_info = {
    'name':'Bulbul',
    'age': 21,
    'fav_movoes': ['Avengers', 'LOR', 'Krish3'],
    'fav_singer' : ['Justin Bieber', 'Shawn Mendes', 'Charlie'],

}
user_info['fav_movoes'].insert(3,'Krish4')

for key , value in user_info.items():
    print(f"{key}: {value}")

user_info['fav_singer'].remove('Justin Bieber')
del user_info['fav_movoes'][2]


print(user_info)

print('----------------')

userinfo_3 = {

}

userinfo_3['name'] = 'zippo'


userinfo_4 = {
    'name':'Alkama',
    'roll_no':'2209'
}

userinfo_3['student2'] = userinfo_4
print(userinfo_3)