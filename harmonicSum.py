def harmonicSum(n):
    if n == 2:
        return 1
    else:
        sum = 1 / (n-1) + harmonicSum(n-1)
        return sum # 1 / n-1 + harmonicSum(n-1)

print(harmonicSum(4))