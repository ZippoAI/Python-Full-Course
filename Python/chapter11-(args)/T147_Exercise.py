




names = ['harshit', 'Mohit']

empty = ""
for i in names:
    empty = i[::-1]
    print(empty.capitalize())
    
print('------------')


# print(name_rev(names))

def name_rev(name, reverse_ = False):
    empty_l = []
    if reverse_ == True:
        for i in name:
             empty_l .append((i[::-1].capitalize()))
        return empty_l
    else:
        for i in name:
            empty_l.append(i.capitalize())
        return empty_l
            
            

print(name_rev(names))

# name_rev(names, reverse_= True)

print('---------------more short------------')
def name_rev2(name, reverse_ = False):
    return [ i[::-1].capitalize() if reverse_ == True else i.capitalize() for i in name]

print(name_rev2(names, reverse_=True))