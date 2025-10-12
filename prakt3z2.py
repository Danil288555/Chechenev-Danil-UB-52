def C(a, b):
    if a < 2 and b > 3:
        return a + b**2
    elif a > b and a > 3:
        return b**2 + 2
    else:
        return b

print(C(1, 4)) 