print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = not (z or (w <= y)) or (x <= z)
                if F == 0:
                    print(x, y, z, w)