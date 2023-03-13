def F(x, y, A):
    return (x < A) or (y < A) or (x + 2*y > 150)


for A in range(0, 100):
    flag = 1
    for x in range(100):
        for y in range(100):
            if F(x, y, A) == 0:
                flag = 0
                break
    if flag:
        print(A)
