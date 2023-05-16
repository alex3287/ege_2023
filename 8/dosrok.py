ABC = 'АВЛОР'
k = 1
for a in ABC:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                word = a+b+c+d
                if a == 'Л':
                    print(k, word)
                k += 1

