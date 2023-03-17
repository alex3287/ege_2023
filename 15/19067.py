def alg(x, y, A):
    return (x + 2*y < A) or (y > x) or (x > 30)


for A in range(90, 100):
    flag = 1
    for x in range(1000):
        for y in range(1000):
            if alg(x, y, A) == 0:
                flag = 0
                break
    if flag:
        print(A)
