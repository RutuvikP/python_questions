def primeCheck(num):
    factorial=0
    for i in range(2,num):
        if num%i==0:
            factorial+=1
    return factorial

output=primeCheck(12)
if(output>0):
    print("Not Prime")
else:
    print("Prime")