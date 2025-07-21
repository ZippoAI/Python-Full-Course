input_value = input(": ")

if len(input_value) > 1:
    print('Its a word')
else:
    if(input_value.isalpha()):
        print('Its Alpha bet')
    elif(input_value.isdigit()):
        print('Its a digit')
    elif(int(input_value).isdecimal()):
        print('its a decimal')
    else:
        print('its a symbol')