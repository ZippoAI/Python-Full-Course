class Person:
    count_instance = 0
    def __init__(self, name):
        self.name = name
        Person.count_instance+=1
    
        




p1 = Person('Zippo')
p2 = Person('Zippo2')

print(Person.count_instance)