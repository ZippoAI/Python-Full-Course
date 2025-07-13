# # # if elif else statement

# # # if we want to check multiple statement then we can use this statement


# age = int(input("Enter your age: "))
# if age == 0 or age < 0:
#     print("Please enter your valid age") 


# if 0<age<=3:
#     print("Ticket price is free")

# elif 3<age<=10:
#     print("Ticket price is 50")

# elif 10<age<=60:
#     print("Ticket price is 150")

# elif 60<age :
#     print("Ticket price is 200")





age = int(input("Enter your age to check ticket price: "))

if 0<age<3:
    print("Ticket is free")
elif(3<age<10):
    print("Ticket price is 150")
elif(10<age<18):
    print("Ticket price is 300")
elif(18<age<=30):
    print("Ticket price is 500")
else:
    print("Cant let you enter old fart")
