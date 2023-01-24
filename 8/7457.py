abc = 'КЛРТ'
k = 0
for a in abc:
    for b in abc:
        for c in abc:
            for d in abc:
                word = a+b+c+d
                k += 1
                print(k, word)