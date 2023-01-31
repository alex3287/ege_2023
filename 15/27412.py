def F(x, A):
    return (x % A != 0) <= ((x % 6 == 0) <= (x % 9 != 0))


for A in range(1, 30):
    for x in range(1, 5000):
        if F(x, A) == 0:
            break
    else:
        print(A)
