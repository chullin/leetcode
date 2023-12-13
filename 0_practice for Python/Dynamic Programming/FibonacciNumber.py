"""
    f(n) = n,               if n <= 1
    f(n) = f(n-1)+f(n-2),   if n >  1
"""

def fibo(x):
    if x <= 1:
        return x
    else:
        return fibo(x-1)+fibo(x-2)
    

n = 45
for i in range(n+1):
    print(fibo(i), end=' ')
print()