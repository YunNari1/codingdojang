def fib(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    return fib(a-1)+fib(a-2)

n=int(input())
print(fib(n))