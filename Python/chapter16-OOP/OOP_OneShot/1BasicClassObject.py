class Car:
    def __init__(self, user_brand, user_model):
        self.brand = user_brand
        self.model = user_model
        
        

my_car = Car("BMW", "M8")

print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")

print(my_new_car.model)