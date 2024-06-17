def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
def gen_fib(n):
    fib=[]
    for i in range(n):
        fib.append(fibonacci(i))
    return fib
n=int(input("Enter Number of terms:"))
result=gen_fib(n)
print(f"Fibonacci upto {n} terms is {result}")
