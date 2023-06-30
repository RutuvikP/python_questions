tuple1 = (11, [22, 33], 44, 55)

for i in tuple1:
    if type(i) is list:
        i[0]=222

print(tuple1)