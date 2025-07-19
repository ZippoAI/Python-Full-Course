

all_user = {
    'user1':{
    'name':'Bulbul',
    'age':30,
    'country':'Japan',
    'state': 'Osaka', 
    'fav movies':['Ironman', 'Batman', 'Superman']
    },

    'user2':{
    'name':'Zippo',
    'age':21,
    'country':'India',
    'state': 'Assam'
    }

}



user3 = {
    'name':'Bulbul',
    'age':30,
    'country':'Japan',
    'state': 'Osaka', 
    'fav movies':['Ironman', 'Batman', 'Superman']
    }



user_four = {
    'name':'ZIPPO',
    'age':21,
    'fav-songs':[],
    'fav-movie':['spiderman','batman']
}

user_four['fav-songs'] = ['yummy','despacito']

user_four.popitem()

print(user_four)
print(UserWarning)