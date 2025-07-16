number1 = [[12], [13], [14]]



# for sublist in number1:
#     emptyL = []
#     for i in sublist:
#        revser_l = int(str(i)[::-1])
#     emptyL.append(revser_l)
#     print(emptyL, end=",")
    
emptyL = []
for sublist in number1[::-1]: #[14] [13] [12]
    for i in sublist:
        rev = []
        rev.append(int(str(i)[::-1]))
    emptyL.append(rev)
print(emptyL)
    