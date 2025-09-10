# Create a laptop class with attributes like brand name, model , price

#Create two objects of you laptop class


class Laptop:
    def __init__(self, brand_name, price, model):
        self.brand_name = brand_name
        self.price = price
        self.model = model
    def __str__(self):
        return f"{self.brand_name} - {self.model} - {self.price}"

l1 = Laptop('Asus', 1500, 'Tuf gaming')

l2= Laptop('Acer', 1000, 'Acer Nitro')


print(l1)
print(l2)