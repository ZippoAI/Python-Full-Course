name = 'ZIPOO'

num = 12345

for i in name:
    print(i)
print('-----------------')
for i in str(num):
    print(i)
print('-----------------')
i = 0
while i<len(name):
    print(name[i])
    i+=1 

i2 = 0
print('-------------')
while i2<len(str(num)):
    print(str(num)[i2])
    i2+=1