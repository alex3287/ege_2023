def alg(N):
    bin_num = bin(N)[2:-1]  # 0b10000
    if N % 2 == 0:
        bin_num = bin_num + '01'
    else:
        bin_num += '10'
    R = int(bin_num, 2)
    return R


for N in range(1, 5000):
    R = alg(N)
    if R == 2017:
        print(N, R)