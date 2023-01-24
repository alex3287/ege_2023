def F(n):
    if n <= 1:
        return n+1
    return n+1 + 2*n + F(n-1) + F(n-3)


for i in range(3, 100):
    result = F(i)
    if result > 1000_000:
        print(i, result)
        break