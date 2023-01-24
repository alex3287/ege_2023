# 1->3; 1+1+1, 1*2+1
# 1->4; 1+1+1+1, 1*2*2, 1+1*2, 1*2+1+1


def F(start, finish):
    if start > finish or start == 17:
        return 0
    if start == finish:
        return 1
    return F(start+1, finish) + F(start*2, finish)


print(F(1, 10) * F(10, 35))