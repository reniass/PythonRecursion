def genSubSets(L):
    res = 0
    if len(L) == 0:
        return [[]]
    smaller = genSubSets(L[:-1])
    print(smaller)
    extra = L[-1:]
    print(extra)

    new = []
    for small in smaller:
        new.append(small + extra)
    print(new)
    print('\n')
    return smaller + new


print(genSubSets([1,2,3]))