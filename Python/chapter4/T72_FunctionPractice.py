# Funtion Practice

'''def last_char(name):
    return name[-1]

print(last_char("Zippo"))'''
    
# --------------------------------

'''def odd_even(numer):
    if numer % 2==0:
        return "Even"
    else:
        return "Odd"

print(odd_even(2))'''
   
# ------------------------
'''
def odd_even(numer):
    if numer % 2==0:
        return "Even"
    return "Odd"
x = int(input("Enter a number: "))
print(odd_even(x))

'''

# --------------------------
'''
def is_even(num):
    if num % 2 ==0:
        return True
    return False

x = int(input("Enter a number: "))

print(is_even(x)) '''

# ----------------------------

'''def greater(a,b):
    if a>b:
        return a
    else:
        return b
    
x =  int(input("enter first number:"))
y =  int(input("enter second number:"))

print(greater(x,y) , "is greater")
'''

#--------------------------------

'''
def cha(name2):
    return name2[-1]

name = input("Enter your name: ")
print(cha(name))'''

#--------------------------------
#Even or odd
'''def even_odd(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"
print(even_odd(5))'''


#--------------------------------
#Find the greateset among three number

'''def greatest(a , b , c):
    if a>=b and a>=c:
        return f"{a} is greateset"
    elif b>=c and b>=a:
        return f"{b} is greateset"
    else:
        return f"{c} is greateset"

print(greatest(8,7,7))'''


#--------------------------------
'''def even_odd(a, b):
    if a%2==0:
        print(f"{a} is Even")
    else:
        print(f"{a} is odd")

    if b%2==0:
        print(f"{b} is Even")
    else:
        print(f"{b} is odd")


  
a , b = map(int, input("Enter two number: ").split(","))

even_odd(a,b)'''


'''def song():
    return "Hello "

print(song())
'''

#--------------------------------
# Greater Number between two numbers: 
'''def greatere(a,b):
    if a<b:
        return b
    return a

num1 , num2 = map(int,input('Enter two numberes using comma in between: ').split(','))

print(greatere(num1,num2))
'''


def greater(a,b):
    if a>b:
        return a
    return b

print(greater(10,90), 'is greater')