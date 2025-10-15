class Person:
    count_instance = 0 #class variable / class attribute
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.count_instance+=1


    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} of person class"


    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above18(self):
        if self.age>=18:
            return f"{self.first_name} is 18+"
        else:
            return f"{self.first_name} is under 18"
    
        




p1 = Person('Zippo', 'Gaming', 20)
p2 = Person('Bulbul', 'Hassan', 17)

print(p1.is_above18())

print(Person.count_instances())