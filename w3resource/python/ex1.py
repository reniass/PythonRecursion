def f(L):
    if len(L) == 1:
        return L[0]
    else:
        return L[0] + f(L[1:])

print(f([1,2,3,45]))
