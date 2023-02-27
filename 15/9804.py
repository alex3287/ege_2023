def F(x, A):
    return (x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0))


for A in range(100):
    flag = 1
    for x in range(1000):
        if F(x, A) == 0:
            flag = 0
            break
    if flag:
        print(A)