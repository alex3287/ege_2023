from sys import setrecursionlimit


setrecursionlimit(2100)


def F(n):
    if n < 4 or n % 2 != 0:
        return 1
    return F(n-1) + F(n-2) + F(n-3)


print(F(2008) - F(2006))