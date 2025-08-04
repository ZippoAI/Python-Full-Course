# Write a program that takes an integer n and prints a right-aligned triangle of stars (*) of height n.

space_count = 5
for i in range(1,5):
    print(f"{space_count * " " }{i * '*'}   ")
    space_count-=1

