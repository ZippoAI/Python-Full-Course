

def check_armstrong(input_number):
    total_digit = len(str(input_number))
    final = 0
    for i in str(input_number):
        final+=int(i)**total_digit
    if final==input_number:
        print('Armstrong Number')
    else:
        print('Not an Armstrong Number')

check_armstrong(153)