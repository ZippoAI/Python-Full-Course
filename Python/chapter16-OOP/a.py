class Laptop:
    sale_discount = 20
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def ApplyDiscount(self):
        discount_amount = (self.sale_discount/100)*self.price
        return f"Total - {self.price} Discount - {self.sale_discount}%({discount_amount} Rs)\nFinal Price - {self.price - discount_amount}\n"


        

l1 = Laptop('Asus', 'Tuf', 200)
l2 = Laptop('Acer', 'Nitro', 670)
l2.sale_discount = 50
print(l2.__dict__)
print(l2.ApplyDiscount())



# print(l2.ApplyDiscount())

print()