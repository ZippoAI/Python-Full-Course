 # Sum : 1 to 10 

i = 1
total = 0

while i <=10:
    total = total+i
    print(f"{total-i}+ {i}  = {total}")
    i+=1

print("---------------------")

total = 0
for i in range(1,11):
    total+=i
    print(f"{total-i} + {i} = {total}")