class Person:
    count_instance = 0
    def __init__(self, name):
        self.name = name
        Person.count_instance+=1
    
    def __str__(self):
        return f"{self.name}\nCount instance: {Person.count_instance}"
    


p1 = Person('Bulbul')
p2 = Person('Zippo')
p2 = Person('Zippo')
p2 = Person('Zippo')
p2 = Person('Zippo')

print(p1)
