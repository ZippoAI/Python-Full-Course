''' Q1: Multiply All Numbers
Create a function my_product(*args)
Return the product of all numbers passed to the function.
If any input is not an int or float, return "Wrong Input '''


'''
my_product(2, 3, 4) → 24  
my_product(2, '3', 4) → "Wrong Input"
'''

def my_product(*args):
    if all([type(arg) == int or type(arg) == float] for arg in args):
        empty = 1
        for num in args:
            empty*=num
        return empty
    else:
        return 'Wrong Input'
    
print(my_product(5,5))
    
'''
📚 Q2: Custom Max Finder
Create a function my_max(*args)
Return the maximum number from the given arguments.
If any input is not a number, return "Wrong Input".

📌 Example:
my_max(2, 8, 1, 4) → 8  
my_max(3, 7, 'a') → "Wrong Input"
'''

