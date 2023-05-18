def maxi_len(number):
    k = 1
    max_k = 1
    s = str(number)
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            k += 1
            max_k = max(max_k, k)
        else:
            k = 1
    return max_k

maxi_l = 1
for i in A:
    maxi_l = max(maxi_l, maxi_len(i))

count = 0
for i in A:
    if maxi_len(i) == maxi_l:
        count += 1