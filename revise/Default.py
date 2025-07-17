number  = 12345
total = 0
for line in str(number):
    for i in line+1:
        print(i, end=" ")
        
        

for i in range(1, 6):          # Outer loop for rows
    for j in range(1, i+1):    # Inner loop for columns
        print(j, end='')       # Print numbers on the same line
    print()                    # Move to next line
