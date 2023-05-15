# m&n
def F(x, A):
    return (x & 39 == 0) or ((x&11==0) <= (x&A!=0))


for A in range(100):
    flag = 1
    for x in range(100):
        if F(x, A) == 0:
            flag = 0
            break

    if flag == 1:
        print(A)