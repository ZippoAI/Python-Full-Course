#OBJECTIVES

'''
What is class

How to create class
    
What is __init__ method 

What are attributes, instance variables

How to create our object
'''


class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('Bulbul', 'Hassan', 21)
p2 = Person('Zippo', 'Gaming', 21)

print(p1.first_name)


