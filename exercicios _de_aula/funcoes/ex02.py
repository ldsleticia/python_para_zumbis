def fatorial(n):
    f = 1
    while n > 0:
        f = f * n
        n = n - 1
    return f


for i in range(5):
    print(fatorial(i))
