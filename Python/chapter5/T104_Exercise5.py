'''Find the common elements between two lists in Python?'''

# Define two lists
list_a = [1,4,5,6]
list_b = [1,2,4,5,6]

# Function to find common elements between two lists
def common_finder(list_1, list_2):
    output = []  # Initialize an empty list to store the common elements

    # Loop through each element in list_1
    for i in list_1:
        # Check if the element is also in list_2
        if i in list_2:
            output.append(i)  # Append the common element to the output list
    
    return output  # Return the list of common elements

# Call the function with list_a and list_b and print the result
print(common_finder(list_a, list_b))  # Output: [1, 2]




