def invert(lst):
    res = []
    for i in lst:
        res.append(i * -1)
    return res


A = []  # [-1,2,-3,4,-5]
print(invert(A))

# def invert(lst):
#    return [i*-1 for i in lst]