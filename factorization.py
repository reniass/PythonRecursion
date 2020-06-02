'''
def factorization(n):

    if n == 1:
        return 1
    else:
        for d in range(2, n+1):
            if n % d == 0:
                 return str(d) + '*' + str(factorization(int(n / d)))




print(factorization(21))
'''
'''
def factorization(n):
    result = []
    if n == 1:
        result.append(1)
        return result
    else:
        for d in range(2, n+1):
            if n % d == 1:
                result.append(d)
                next_factor = factorization(int(n/d))
                result.append(next_factor)
    return result

print(factorization(21))
'''




