#Kwargs Keyword Argument

# ** Kwargs (Double star operator)


# kwargs as parameter

def func( **kwargs):
    for k , v in kwargs.items():
        print(f"{k} : {v}")

print(func( firstname = 'Bulbul', lastname = 'Hassan'))


def func(name, **kwargs):
    for k , v in kwargs.items():
        print(f"{k} : {v}")

print(func("Bulbul Hassan" , firstname = 'Bulbul', lastname = 'Hassan'))

#Dictionary Unpacking
print('-------Dictionary Unpacking------------')
print()
d = {'Name':'Zippo',
     'age':21
     }


def func( **kwargs):
    for k , v in kwargs.items():
        print(f"{k} : {v}")

print(func(**d))