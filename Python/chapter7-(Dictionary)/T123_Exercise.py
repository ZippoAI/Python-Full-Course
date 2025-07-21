name = input("Enter Your Name: ")
age = input("Enter Your Age: ")
fav_movies = input('Enter You favorite Movies comma separated: ').split(",")
fav_song= input('Enter Your favorite songs: ').split(",")


user_info = dict(name = name, age = age, fav_movie = fav_movies, fav_songs = fav_song)


for  key, value in user_info.items():
    print(f"{key}:{value}")
