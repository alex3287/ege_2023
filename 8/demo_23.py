abc = '01234567'
k = 0
for a in abc[1:]:
    for b in abc:
        for c in abc:
            for d in abc:
                for e in abc:
                    number = a+b+c+d+e
                    if number.count('6') == 1:
                        if e == '6' and d in '0246':
                            print(number)
                            k += 1
                        elif a == '6' and b in '0246':
                            print(number)
                            k += 1
                        elif b == '6' and c in '0246' and a in '0246':
                            print(number)
                            k += 1
                        elif c == '6' and b in '0246' and d in '0246':
                            print(number)
                            k += 1
                        elif d == '6' and c in '0246' and e in '0246':
                            print(number)
                            k += 1
print(k)