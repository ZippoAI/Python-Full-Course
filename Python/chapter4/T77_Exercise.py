# name = "naman"

# name2 = name == name[::-1]

# print(name2)

def is_palindrome(name):
    if name == name[::-1]:
        return 'Palindrome'
    else:
        return 'Not Palindrome'


nm = input(': ')

print(is_palindrome(nm))