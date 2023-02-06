print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (z and (w <= y)) and (not x)
                if F:
                    print(x, y, z, w)

# A -> B = not A or B
