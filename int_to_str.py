def intToStr(n, base):
    convert_to_string = '0123456789ABCDEF'
    how_many_base = 1
    diff = 0
    if n < base:
        diff = 
        return convert_to_string[n]
    else:
        how_many_base *= 16
        return intToStr(n // base, base)

