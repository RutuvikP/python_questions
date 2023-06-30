def fact(num):
    if num<0:
        print("Sorry, factorial doesn't exist for negative numbers")
    elif num==0:
        print("Factorial of 0 is 1")
    else:
        factorial=1
        for i in range(1,num+1):
            factorial=factorial*i
        print("Factorial is", factorial)

fact(5)