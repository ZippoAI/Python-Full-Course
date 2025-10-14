class Laptop:
    sale_discount = 20
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def DiscountPrice(self):
        discount_amount = (Laptop.sale_discount/100)*self.price
        return f"Total - {self.price} Discount - {Laptop.sale_discount}%({discount_amount} Rs)\nFinal Price - {self.price - discount_amount}\n"


        

l1 = Laptop('Asus', 'Tuf', 200)
l2 = Laptop('Acer', 'Nitro', 670)

print(l1.brand_name)

print(l2.DiscountPrice())

print()