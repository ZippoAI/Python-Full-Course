class Laptop:
    discount1= 10
    discount2 = 15
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name= model_name
        self.price = price

    def __str__(self):
        return f"{self.brand_name} - {self.model_name} - {self.price}"
    
    def apply_discount(self):
        if self.brand_name[0].lower() == 'a':
            apply_discount = Laptop.discount1
        else:
            apply_discount = Laptop.discount2
        discount_price = self.price * apply_discount/100
        return f"Laptop price: {self.price}\nDiscount price: {discount_price}\nFinal price: {self.price-discount_price}"
    

l = Laptop('bsus', 'Tuf', 1000)

print(l)
print(l.apply_discount())
