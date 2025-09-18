class Laptop:
    def __init__(self, brand_name, model, price):
        self.brand_name = brand_name
        self.model = model
        
        if price>0:
            self._price = price
        else:
            self._price = 0
    @property
    def full_name(self):
        return f"{self.brand_name} - {self.model} - {self.price}"
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = max(new_price, 0)

    

laptop1 = Laptop('asus', 'vivo book', 1000)

laptop1.price = 400


print(laptop1.price)
print(laptop1.full_name)

