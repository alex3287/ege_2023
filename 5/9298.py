def alg(N):
    x1 = N // 100
    x2 = N // 10 % 10
    x3 = N % 10
    first = x1 + x2
    second = x3 + x2
    result = str(max(first, second)) + str(min(first, second))
    return result


for i in range(100, 1000):
    R = alg(i)
    if R == '1715':
        print(R)
