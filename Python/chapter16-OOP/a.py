class Laptop:
    discount = 10
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def __str__(self):
        return f"{self.brand_name} - {self.model_name} - {self.price}"

    def apply_discount(self):
        discount_amount = self.price * Laptop.discount/100
        return f'Total price - {self.price}\nDiscount amount - {discount_amount} \nFinal price - {self.price - discount_amount}'
    

l = Laptop('Asus', 'Tuf Gaming', 1000)

print(l)

print(l.apply_discount())
