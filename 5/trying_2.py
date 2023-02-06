def F(N):
    bin_num = bin(N)[2:]
    suma = bin_num.count('1')
    if suma % 2 == 0:
        bin_num = '1' + bin_num[2:] + '0'
    else:
        bin_num = '11' + bin_num[2:] + '1'
    R = int(bin_num, 2)
    return R


for N in range(1, 100):
    R = F(N)
    if R > 49:
        print(N, R)
