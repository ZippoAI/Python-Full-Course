Total_vowel = ['a','e','i','o','u']

name_check = 'ZiPPOoU'

lower_name = name_check.lower()



def vowelCheck(vowel,name):
    vowelz = []
    for vowel_z in name:
        if vowel_z in vowel:
            vowelz.append(vowel_z)
    return vowelz
    
print(f"Name: {name_check} -  {vowelCheck(Total_vowel,lower_name)}")
