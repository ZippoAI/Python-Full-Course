class Phone:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self._price = price

    def make_a_call(self, phone_number):
        return(f"Calling {phone_number}.....")

    def full_name(self):
        return f"{self.brand_name} {self.model_name}"
    

phone1 = Phone('Nokia', '1100', 1000)

print(phone1._price)
phone1._price = -1000
print(phone1._price)

print()
print('-------------------------------')

l = [3,4,1,2]

l.sort() 


print(l)

p1 = Phone('iphone', '14 pro max', 1400)

print(Phone.make_a_call(p1,9101600489))
print(p1.make_a_call(9101600489))