list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
output=[]

for char in list1:
    for j in list2:
        output.append(char+" "+j)

print(output)