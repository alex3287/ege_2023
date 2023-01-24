abc = 'СЛОН'
k = 0
for a in abc:
    for b in abc:
        for c in abc:
            for d in abc:
                for e in abc:
                    word = a+b+c+d+e
                    if word.count('С') == 1:
                        print(word)
                        k += 1
print(k)