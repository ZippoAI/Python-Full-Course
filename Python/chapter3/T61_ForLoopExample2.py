num = input("Enter a number: ")
total = 0
for i in range (0, len(num)):
    total = total + int(num[i])
    print(total)