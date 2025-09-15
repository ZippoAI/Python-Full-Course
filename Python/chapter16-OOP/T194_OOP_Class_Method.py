# Class methods 
# Difference between class methods and instance methods 

class Person:
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instance+=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances"

    def __str__(self):
        if self.age>=18:
            message = "You are above 18"
        else:
            message = 'You are below 18'
        return f"{self.first_name} {self.last_name}\n{message}"
    
        

person1 = Person('Bulbul', 'Hassan', 18)
person1 = Person('Bulbul', 'Hassan', 18)
person1 = Person('Bulbul', 'Hassan', 18)
print(person1)

print(Person.count_instances())