str1 = "PyNaTive"
lower = "abcdefghijklmnopqrstuvwxyz"

bag1=''
bag2=''

for char in str1:
    if char in lower:
        bag1+=char
    else:
        bag2+=char

print(bag1+bag2)