class Car:
    def __init__(self, user_brand, user_model):
        self.brand = user_brand
        self.model = user_model

    def full_name(self):
        return f"{self.brand} {self.model}"



        
        

my_car = Car("BMW", "M8")

print(my_car.full_name())


my_new_car = Car("Tata", "Safari")

# print(my_new_car.model)