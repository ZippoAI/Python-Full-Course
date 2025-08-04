# Given a number, return the **sum of its digits**. Use a loop.
# **Input:** `n = 1234`

# **Output:** `10`

# for loop
count = 0
num = 1234
for i in str(num):
    count = count + int(i) 
print(count)

# While loop

i2 = 0
count2 = 0

while i2<len(str(num)):
    count2 = count2 + int(str(num)[i2])
    i2+=1
print(count2)
