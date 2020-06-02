def pascal_triangle(n):
    if n == 1:
        return [1]
    else:
        raw = [1]
        previous_raw = pascal_triangle(n-1)
        for e in range(len(previous_raw)-1):
            raw.append(previous_raw[e] + previous_raw[e+1])
        raw.append(1)
        return raw

print(pascal_triangle(6))
