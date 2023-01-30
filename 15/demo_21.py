def F(x, A):
    return ((x % A != 0) <= ((x % 6 == 0) <= (x % 9 != 0)))


for A in range(1, 100):
    for x in range(1, 100):
        if F(x, A) == 0:
            break
    else:
        print(A)
