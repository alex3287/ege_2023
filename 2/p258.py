from itertools import *

def f(x,y,w,z):
    return not(( ( (not w) <= (not y) ) <= (not z)) <= x)

for a in product([0,1], repeat = 5):
    table = [ ( a[0], a[1], 1, 0 ), ( a[2], 1, a[3], 1, ), ( 0, 1, a[4], 0 )]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [ f(**dict(zip(p, row))) for row in table ] == [ 1,1,0 ]:
                print(p)
