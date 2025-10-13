class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name + ' ' +model_name


laptop1 = Laptop('Asus', 'Tuf', 1500)
laptop2 = Laptop('Acer', 'Nitro', 1000)

print(laptop1.brand_name)
        
print(laptop1.laptop_name)