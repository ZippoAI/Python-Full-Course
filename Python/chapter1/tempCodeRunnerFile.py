arr = list(map(int,input("Enter number using comma in between: ").split(",")))
arr2 = list(map(int,input("Enter number using comma in between: ").split(",")))

arr_1= sorted(set(arr))
arr_2= sorted(set(arr2))

print(arr_1, arr_2)