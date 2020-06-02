def f(n):
    s = str(n)
    if len(s) == 1:
        return int(s)
    else:
        return int(s[0]) + f(int(s[1:]))


print(f(345))