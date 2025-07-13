# Function Practice

# def name(a):
#     return a[-1]


# print(name("ZIPO"))


# ------------------------------------------

# def odd_even(a):
#     if a%2==0:
#         return "even"   
#     return "odd"
    


# print(odd_even(3))

# --------------------------------------------

def greater(a,b):
    if a > b:
        return a
    else:
        return b
    

# def greatest(x,y,z):
#     output = greater(x,y)
#     return greater(output,z)


# print(greatest(1,10,6))



# def greatest_r(a,b,c):
#     if a>b and a > c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
    
# print(greatest_r(555,4444,16))


def is_palindrome(name):
    if name[::-1] == name:
        return True

    return False

print(is_palindrome("PIP"))