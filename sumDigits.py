def sumDigits(n):
    if str(n) == 1:
        return n
    else:
        string = str(n)
        return int(string[0]) + sumDigits(int(string[1:]))



print(sumDigits(234))