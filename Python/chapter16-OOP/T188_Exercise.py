class Laptop:
    def __init__(self, brand_name, model, price):
        self.brand_name = brand_name
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.brand_name} - {self.model} - ${self.price}"

    def discount(self, value):
        discount_amount = self.price * value/100
        return f"Discount Amount - ${discount_amount} \nFinal Price - ${self.price - discount_amount }"
        
    

l = Laptop('Asus', 'Tuf Gaming', 100)

print(l)

print(l.discount(10))