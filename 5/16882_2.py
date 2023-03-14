# ____ ____
# 1111 1111
# 5 -> 101 => 0000 0101
# 5 => 5000
# 1000 0000
# 0000 1010
def alg(N):
    bin_num = bin(N)[2:]
    size = len(bin_num)
    zero = 8 - size
    bin_num = '0'*zero + bin_num

    bin_num = bin_num.replace('1', '*')
    bin_num = bin_num.replace('0', '1')
    bin_num = bin_num.replace('*', '0')
    R = int(bin_num, 2)
    # s = ''
    # for i in bin_num:
    #     if i == '1':
    #         s += '0'
    #     else:
    #         s += '1'
    return R - N


for N in range(256):
    R = alg(N)
    if R == 111:
        print(N, R)