'''Q: How can you separate even and odd numbers in a given range and then combine them into a list of lists in Python?

Explanation:
In this example, we are separating even and odd numbers from the range 1 to 7 and then combining them into a list of lists.'''


# Initialize empty lists for even and odd numbers
even_empty = []
odd_empty = []

# Loop through the range from 1 to 7
for i in range(1, 8):
    if i % 2 == 1:  # Check if the number is odd
        odd_empty.append(i)  # Append odd number to odd_empty
    if i % 2 == 0:  # Check if the number is even
        even_empty.append(i)  # Append even number to even_empty

# Combine the even and odd lists into a list of lists
empty2 = [odd_empty] + [even_empty]

# Print the individual lists and the combined list
print('Even:', even_empty)  
print('Odd:', odd_empty)    
print('Combined:', empty2)
 






