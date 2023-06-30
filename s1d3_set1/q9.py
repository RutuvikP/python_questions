def fib(num):
    fibonacci_seq = []
    
    if num >= 1:
        fibonacci_seq.append(0)
    
    if num >= 2:
        fibonacci_seq.append(1)
    
    for i in range(2, num):
        fibonacci_seq.append(fibonacci_seq[i-1] + fibonacci_seq[i-2])
    
    print(fibonacci_seq)

fib(10)
