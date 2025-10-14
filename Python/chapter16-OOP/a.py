class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def DiscountPrice(self,discount_):
        discount_amount = (discount_/100)*self.price
        return f"Total - {self.price} Discount - {discount_}%({discount_amount} Rs)\nFinal Price - {self.price - discount_amount}\nDiscount amount"


        

l1 = Laptop('Asus', 'Tuf', 200)

print(l1.brand_name)

print(l1.DiscountPrice(20))