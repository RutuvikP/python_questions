list1=[("John", 25), ("Jane", 30)]
output=""

for tup in list1:
    output+=tup[0]+" is "+str(tup[1])+" years old."

print(output)