def f(base, power):
    if power == 1:
        return base
    else:
        return base * f(base, power - 1)

print(f(3, 4))