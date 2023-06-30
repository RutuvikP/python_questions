list1=[2, 7, 11, 15]
target=9
n=len(list1)

for i in range(n):
    for j in range(i+1,n):
        if list1[i]+list1[j] == target:
            print(i,j)