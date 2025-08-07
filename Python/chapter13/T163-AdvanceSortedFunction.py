fruits = ['Grapes', 'Apples', 'Mango']
sorted_ = sorted(fruits)
print(sorted_)


fruits2 = ('Grapes', 'Apples', 'Mango')

sorted_2 = sorted(fruits2)

print(sorted_2)

fruits3 = {'Grapes', 'Apples', 'Mango'}


sorted_3 = sorted(fruits3)

print(sorted_3)

print('---------------------')

cars = [
    {'model': 'BMW', 'price': 4000},
    {'model': 'Toyota', 'price': 300000},
    {'model': 'Audi', 'price': 5000},
]

final = sorted(cars, key = lambda model : model['price'], reverse=True)

for i in final:
    print(i)