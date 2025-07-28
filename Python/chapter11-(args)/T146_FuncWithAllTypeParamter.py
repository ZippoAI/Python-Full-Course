# Function with all type of parameter 
# Very Important to understand

#PADK

# if we want to use all these togehter then we have write in below order

#Parameters
# args
# default parameters
# kwargs 

# this is the order
def func(name, *args, last_name = 'Unkown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('bulbul', 1,2,3,4, a = 1, b= 2)