f = [0 for i in range(100)]

def fibo(n):
    if f[n]:
        # print("f[n] = ",f[n])
        return f[n]
    if n <= 1:
        return n
    f[n] = fibo(n-1) + fibo(n-2)
    return f[n]


n = 45
for i in range(n+1):
    print(fibo(i))
    # fibo(i)
# print()


# for i in range(45):
#     print(f[i])