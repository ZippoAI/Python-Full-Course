class Car:
    def __init__(self, user_brand, user_model):
        self.brand = user_brand
        self.model = user_model

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size



my_car = Car("BMW", "M8")

print(my_car.full_name())
