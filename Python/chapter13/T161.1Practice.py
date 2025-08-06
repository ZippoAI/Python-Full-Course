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

def maximum_finder(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        empty= max(args)
        return empty
    else:
        return 'Wrong Input'
    
print(maximum_finder(1,23,4,5,30,'SD'))




'''Q3: Average of Numbers
Create a function find_average(*args)
Return the average of all the numbers passed.
If any non-numeric input is detected, return "Wrong Input".

📌 Example:
find_average(1, 2, 3, 4) → 2.5  
find_average(3, 'x') → "Wrong Input"

'''

def find_average(*args):
    true = []
    total = 0
    for arg in args:
        if type(arg) == int or type(arg) == float:
            true.append(True)
        else:
            true.append(False)

    if all(true):
        total = sum(args)
        return total/len(args)
    else:
        return 'Wrong Input'
l12 = [1,23,4,5]   
print(find_average(10,6,'j'))
print(find_average(*l12))



''' Q4: Count Positives and Negatives
Create a function count_signs(*args)
Return a dictionary with the count of positive and negative numbers.
Ignore 0. If any input is not a number, return "Wrong Input".

count_signs(1, -2, -5, 4, 0) → {'positive': 2, 'negative': 2}  
count_signs(1, 'abc') → "Wrong Input"
'''

def count_number(*args):
    pos_count = 0
    neg_count = 0
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        for num in args:
            if num>0:
                pos_count+=1

            else:
                neg_count+=1

        return  f"Positive: {pos_count}, Negative: {neg_count}"
    else:
        return 'Wrong Number'



                


        
print(count_number(2,4,-1,-2))


