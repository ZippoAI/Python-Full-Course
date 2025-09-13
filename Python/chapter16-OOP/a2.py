class Laptop:
    discount = 10
    discount2 = 15
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def __str__(self):
        return f"{self.brand_name} - {self.model_name} - {self.price}"

    def apply_discount(self):
        if self.brand_name[0].lower() == 'a':
            discount_amount =  Laptop.discount
        else:
            discount_amount = Laptop.discount2
            
        discount_amount = self.price * discount_amount/100
        return f'Total price - {self.price}\nDiscount amount - {discount_amount} \nFinal price - {self.price - discount_amount}'
        

l = Laptop('HP', 'Victus', 98999)
l2 = Laptop('Asus', 'ROG Strix G16', 113990)

print(l)
print(l.apply_discount())
print('---------------------')
print(l2)


print(l2.apply_discount())


