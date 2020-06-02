def harmonicSum(n):
    if n == 2:
        return float(1)
    else:
        return float(1/n-1) + harmonicSum(n-1)

print(harmonicSum(5))