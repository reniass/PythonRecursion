def g_c_d(a, b):
    if b % a == 0:
        return a
    else:
        return g_c_d(b % a, a)

print(g_c_d(4, 16))