name = input("Enter your name: ")

password = input("Enter your password: ")

confirm_password = input("Confirm your password: ")


while True:
    if password!=confirm_password:
        print('you entered wrong password')
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")
    else:
        break

while True:
    print('Lets login')
    username = input('Enter your username: ')
    userpassword = input('Enter your password: ')
    
    if name != username:
        print('you entered wrong username')
    elif userpassword!=password:
            print('you entered wrong password')             
    else:
        print('Login succesfull')
        break
