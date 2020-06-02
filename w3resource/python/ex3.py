def f(L):
    if len(L) == 1:
        if type(L[0]) == int:
            return L[0]
        elif type(L[0]) == list:
            return L[0][0]
        else:
            raise ValueError
    else:
        if type(L[0]) == int:
            return L[0] + f(L[1:])
        elif type(L[0]) == list:
            return L[0][0] + f(L[1:])
        else:
            raise ValueError

print(f([1,2,[3,4],[5,6]]))