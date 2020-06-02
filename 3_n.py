def three_n(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3
    else:
        return 3 + three_n(n-1)

print(three_n(10))