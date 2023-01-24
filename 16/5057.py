def F(n):
    if n < 3:
        return 3
    return 5*F(n-1) - 4*F(n-2)


print(F(15))