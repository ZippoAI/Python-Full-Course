#looping in tuples 
# tuples with one element
# tuples without parenthesis
# tuples unpacking
# list inside tuple
# some function that you can use with tuples


mixed = (1,2,3,4,5.0)

#for loop and tuple
for i in mixed:
    print(i)

# tuples with one element
num = (1) #Its a integer
words = ('words') #Its a string

num  =(1,) #after adding , it becomes tuples


print('----Tuples Withut parenthesis----')

cars = 'BMW', 'AUDI', 'TATA'


print('------Tuple Unpacking------')

# Tuple of singers
singers = ('Justin Bieber', 'Shawn Mendes', 'Bruno Mars')

# Tuple unpacking: Each element of the tuple is assigned to a separate variable
singer1, singer2, singer3 = singers

# Now:
# singer1 = 'Justin Bieber'
# singer2 = 'Shawn Mendes'
# singer3 = 'Bruno Mars'

# This is called tuple unpacking in Python.
# The number of variables on the left must match the number of elements in the tuple.

print(singer1)  # Output: Justin Bieber
print(singer2)  # Output: Shawn Mendes
print(singer3)  # Output: Bruno Mars



#List inside tuples, We cant change the tuples but we can change the list that is inside the tuple
fruits = ('apple', 'mango', ['Banana', 'Kiwi'])

fruits[2].pop()

print(fruits)


print(sum(mixed))