def evkl(a, b):
    while b != 0:
        a, b = b, a % b
    return a

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))

ch = A * D
zn = B * C

sokr = evkl(ch, zn)
ch //= sokr
zn //= sokr

print(f"{ch}/{zn}")