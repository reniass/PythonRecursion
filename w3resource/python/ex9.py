def f(a1, q, n):
    if n == 2:
        return a1
    else:
        return a1*q**(n-2) + f(a1, q, n-1)

print(f(1,2, 5))
