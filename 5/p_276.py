def alg(N):
    # sn = str(N)
    s1 = sum([int(i) for i in str(N) if int(i) % 2 == 0])
    s2 = sum([int(j) for i, j in enumerate(str(N)) if i % 2 == 0])
    # for i, j in enumerate(sn, 1):
    #     if i % 2 != 0:
    #         s2 += int(j)
    # s1 = 0
    # for i in str(N):
    #     if int(i) % 2 == 0:
    #         s1 += int(i)
    R = abs(s1-s2)
    return R


# print(alg(9294))
for N in range(100, 100_000):
    R = alg(N)
    if R == 27:
        print(N, '->', R)
        # break