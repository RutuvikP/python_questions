def reverseStr(str):
    bag=""
    for i in range(len(str)-1,-1,-1):
        bag+=str[i]
    return bag

output=reverseStr("Python")
print(output)