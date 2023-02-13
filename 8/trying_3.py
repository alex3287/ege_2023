ABC = '012345678'
count = 0
for a in '2468':
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    for f in ABC:
                        for g in '1357':
                            number = a+b+c+d+e+f+g
                            if number.count('8') == 1:
                                count += 1
print(count)
