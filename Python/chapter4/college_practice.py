# print("*")
# print("**")
# print("***")
# print("****")
# i = 10
# total =0

# while i>0:
#     # total+=i
#     i-=1
#     print(i * "*")


# name = "zipgo"

# print(name[3::-1])

# name = "zippo"

# for i in range(0,len(name)):
#     print(name[i])

name = input("Enter a number: ")
total = 0
i = 0
while i<len(name):
    total+= int((name[i]))
    i+=1
print(total)