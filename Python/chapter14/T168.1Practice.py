
 # Create a function make_multiplier(n) that returns a function which multiplies its input by n.

'''
double = make_multiplier(2)
print(double(10))   # Output: 20

triple = make_multiplier(3)
print(triple(7))    # Output: 21
'''

def multiplier(n):
    def total(x):
        return x*n
    return total

double = multiplier(2)
print(double(10))

#Q3. Custom Adder
#Write a function make_adder(n) that returns a function which adds n to its argument.

'''
add5 = make_adder(5)
print(add5(10))   # Output: 15

add100 = make_adder(100)
print(add100(50)) # Output: 150

'''

def adder(x):
    def total(y):
        return x+y
    return total

add5 = adder(5)
print(add5(10))


# Q4. String Repeater
# Write a function string_repeater(n) that returns a function which repeats a given string n times.

'''
repeat3 = string_repeater(3)
print(repeat3("Hi"))   # Output: HiHiHi

repeat5 = string_repeater(5)
print(repeat5("A"))    # Output: AAAAA

'''

def string_repeater(x):
    def repeat(string):
        return string*x
    return repeat

times2 = string_repeater(2)
print(times2('Hi')) 


# Q5. Range Checker

# Write a function range_checker(low, high) that returns a function which checks if a number is inside the given range.

'''
check = range_checker(10, 20)
print(check(15))   # Output: True
print(check(25))   # Output: False

'''

def range_(lower,bigger):
    def range_checker(number):
        return lower <=number <= bigger
    return range_checker

ranger = range_(10,20)

print(ranger(15))
