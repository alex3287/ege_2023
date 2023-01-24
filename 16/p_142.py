from sys import setrecursionlimit


setrecursionlimit(5100)


def F(n):
    if n**0.5 == int(n**0.5):
        return n**0.5
    return F(n+1) + 1


print(F(4850) + F(5000))