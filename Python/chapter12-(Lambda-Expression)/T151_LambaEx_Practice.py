#Lamda Expression Practice

def is_even(a):
    return a % 2 == 0

print(is_even(3))



# same function with lamba expression
is_even2 = lambda a : a%2 ==0
print(is_even2(3))

print('------------')

last_Char = lambda a : a[-1]

print(last_Char('ZiPPO'))

print('-------Lamba with if else---------------')

# lambda with if , else
def func(s):
    if len(s)>5:
        return True
    else:
        return False
    
func1 = lambda a : True if len(a)>5 else False
# more short
func2 = lambda a : len(a)>5 

print(func1('H'))