#Class Method as Constructor


class Person:
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instance+=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    @classmethod
    def from_string(cls, string):
        first,last,age = string.split(',')
        return cls(first,last,int(age))


    @classmethod
    def total_instance(cls):
        return f"You have created {cls.count_instance}"


    def __str__(self):
        if self.age>=18:
            message = "You are above 18"
        else:
            message = 'You are below 18'
        return f"{self.first_name} {self.last_name}\n{message}"
    
    @staticmethod
    def hello():
       return('Hello')
    
    
        
# Usually, we create an object like this:
person1 = Person('Bulbul', 'Hassan', 18)

# But if we want to pass all the data in a single string,
# we can do something like this:
p3 = Person.from_string('Bulbul, HassaM, 24')


# print(person1)
print(p3)


print(Person.total_instance())

print(Person.hello())
