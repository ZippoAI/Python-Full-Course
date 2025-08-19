# Function Returning Function (Closure) Practice

def to_power(x):
    def calculate_power(a):
        return a*x
    return calculate_power

cube = to_power(3)

print(cube(5))
