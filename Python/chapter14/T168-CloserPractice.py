# Function Returning Function (Closure) Practice

def to_power(x):
    def calculate_power(n):
        return n**x
    return calculate_power

cube = to_power(3)
print(cube(5))


square = to_power(2)

print(square(4))