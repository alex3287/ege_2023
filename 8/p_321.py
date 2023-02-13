
ABC = '0123456789abcdefghijklmnopqrstuvwxyzABCDEF'
ABC2 = '02468acegikmoqsuwyACE'
count = 0
for a in ABC[1:]:
    print('a', a)
    for b in ABC:
        print('b', b)
        for c in ABC:

            for d in ABC:
                for e in ABC:

                    for f in ABC:
                        number = a+b+c+d+e+f
                        if number.count('6') == 1:
                            if a == '6' and b in ABC2:
                                count += 1
                            elif f == '6' and e in ABC2:
                                count += 1
                            elif b == '6' and a in ABC2 and c in ABC2:
                                count += 1
                            elif c == '6' and b in ABC2 and d in ABC2:
                                count += 1
                            elif d == '6' and c in ABC2 and e in ABC2:
                                count += 1
                            elif e == '6' and d in ABC2 and f in ABC2:
                                count += 1


print(count)

