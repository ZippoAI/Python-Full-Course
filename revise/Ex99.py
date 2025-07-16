number = [1,2,3,4,5,6,7,8,9]

def find_odd_eve(l):
    odd_L = []
    even_L = []
    for sublist in l:
        if sublist%2==0:
            even_L.append(sublist)
        else:
            odd_L.append(sublist)
    return [even_L]+[odd_L]
    
    
    

print(find_odd_eve(number))
