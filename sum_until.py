def sumUntil(n):
    if n == 0:
        return 0
    else:
        return n + sumUntil(n-2)


print(sumUntil(6))