def multiplu_ (*args):
    total = 1
    for i in args:
        total*=i
    return total

new_list = [1,2,3]
print(multiplu_(*new_list))