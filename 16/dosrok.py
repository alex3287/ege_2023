def F(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n + 3 + F(n+3)


print(F(2000))