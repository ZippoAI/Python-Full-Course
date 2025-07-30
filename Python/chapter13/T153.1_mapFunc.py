# Map Function - map(function, iterable)
#              - Returns an interator that applies functuion to every time of iterable

def make_even(num):
    if num%2 ==1:
        return num+1
    else:
        return num
    
x = [523,235,543,234,223,243,234,436]

y = list(map(make_even, x))

print(y)