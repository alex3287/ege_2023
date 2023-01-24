def shortcut(s):
    abc = 'aeiou'
    s2 = ''
    for i in s:
        if i not in abc:
            s2 += i
    return s2


s = 'hello aklsfdjasm,n ,mn.'  # hll
print(shortcut(s))


# def sequence_sum(start, end, step):фвыафы
#     return sum(range(start, end+1, step))