def alg(N):
    bin_num = bin(N)[2:]
    zero = 8 - len(bin_num)
    s = '0' * zero
    bin_num = s + bin_num
    new = ''
    for i in bin_num:
        if i == '0':
            new += '1'
        else:
            new += '0'
    R = int(new, 2)
    R = R - N
    return R


for N in range(256):
    R = alg(N)
    if R == 111:
        print(N, R)