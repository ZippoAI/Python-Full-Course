# num1, num2, num3, num4= input("Enter Four number comma split: ").split(",")
# print(f"Your total is {int(num1) + int(num2) + int(num3)+ int(num4)}")


a , b , c = map(int, input("Enter three numbers comma separeted: ").split(","))

# average = ((int(a) + int(b) + int(c) ) / 3)
average = (a + b + c) /3
print(int(average))

#The map function in Python applies a given function to all items in an input list (or any other iterable) and returns a map object (an iterator) containing the results. It is commonly used to apply a function (like int) to each element in an iterable (like a list of strings).


