ABC = 'АЕКМНЬ'
k = 0
for a in ABC:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    for f in ABC:
                        word = a + b + c + d + e + f
                        k += 1
                        if word.count('М') == 2 and word.count('A') < 2 and a != 'Ь':
                            print(k, word)


# НЬЬЬММ
