def F(x, A):
    return ((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 100)


for A in range(1, 200):
    flag = 1
    for x in range(1, 1000):
        if F(x, A) == 0:
            flag = 0
            break
    if flag == 1:
        print(A)