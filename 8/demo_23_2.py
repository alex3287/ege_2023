ABC = '01234567'
ABC2 = '1357'
count = 0
for a in ABC[1:]:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    number = a+b+c+d+e
                    if number.count('6') == 1:
                        index = number.index('6')
                        print(number[index-1:index+2], number)
                        # if e == '6' and d not in '1357':
                        #     count += 1
                        #     print(number)
                        # elif a == '6' and b not in ABC2:
                        #     count += 1
                        #     print(number)
                        # elif b == '6' and a not in ABC2 and c not in ABC2:
                        #     count += 1
                        #     print(number)
                        # elif c == '6' and b not in ABC2 and d not in ABC2:
                        #     count += 1
                        #     print(number)
                        # elif d == '6' and c not in ABC2 and e not in ABC2:
                        #     count += 1
                        #     print(number)
# print(count)