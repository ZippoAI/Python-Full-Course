name = input(": ")

empty_var = ""

for i  in range(len(name)):
    if name[i] not in empty_var:
        empty_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}4")