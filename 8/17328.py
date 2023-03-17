abc = 'ГЕРАСИМ'
abc2 = 'ЕАЕИАЕАИИАИЕ'
for a in abc:
    for b in abc:
        for c in abc:
            for d in abc:
                for e in abc:
                    for f in abc:
                        for g in abc:
                            word = a+b+c+d+e+f+g
                            if (word.count('Г') == 1 and word.count('Е') == 1 and word.count('Р') == 1 and
                                    word.count('А') == 1 and word.count('С') == 1 and
                                    word.count('И') == 1 and word.count('М') == 1):
                                if 
