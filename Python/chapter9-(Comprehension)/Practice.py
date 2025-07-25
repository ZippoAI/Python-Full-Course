

even_square = [i*i for i in range(1,21) if i%2 == 0]

print(even_square)



words = ['apple', 'Banana', 'Avocado', 'Grape', 'Apricote']
FilterWord = [i for i in words if i[0]== 'a' or i[0] == 'A']

print(FilterWord)

celcius = [0, 10, 20, 30, 40]
Celcius_to_fahreneheit = [(i * 9/5)+32 for i in celcius]

print(Celcius_to_fahreneheit)