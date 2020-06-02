def sum_first_integers(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum_first_integers(n-1)


print(sum_first_integers(12))