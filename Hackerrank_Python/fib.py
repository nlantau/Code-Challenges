# nlantau, 2021-01-18

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fib(n):
    l = [None] * (n+1)
    l[0] = 0
    l[1] = 1
    l[2] = 1
    for i in range(2,n+1):
        l[i] = l[i-1] + l[i-2]
    return l[n]

n = 2
k = 1
#print(fib(n))


print(fibonacci(n))
print(fibonacci(k))