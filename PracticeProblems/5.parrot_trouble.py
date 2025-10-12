def parrot_trouble(talking, hour):
    if talking:
        if hour<7 or hour>20:
            return True
        else:
            return False
        
    else:
        return False
    

  
#Second approach

def parrot_trouble(talking, hour):
    if talking and (hour<7 or hour>20):
        return True
    else:
        return False
    

# third approach

def parrot_trouble(talking, hour):
    return talking and (hour<7 or hour>20)