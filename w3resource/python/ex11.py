def gcd(number1, number2):
    if number1 <= number2:
        if number2 % number1 == 0:
            return number1
        else:
            return gcd(number2 % number1, number2 // number1)
    else:
        if number1 % number2 == 0:
            return number2
        else:
            return gcd(number1 % number2, number2 // number1)


print(gcd(5, 65))