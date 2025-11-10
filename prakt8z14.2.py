n = int(input("Введите n: "))
matrix = [[0] * n for _ in range(n)]

num = 1
verh, dno = 0, n - 1
left, right = 0, n - 1

while num <= n * n:
    for i in range(left, right + 1):
        matrix[verh][i] = num
        num += 1
    verh += 1
    
    for i in range(verh, dno + 1):
        matrix[i][right] = num
        num += 1
    right -= 1
    
    for i in range(right, left - 1, -1):
        matrix[dno][i] = num
        num += 1
    dno -= 1
    
    for i in range(dno, verh - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

for row in matrix:
    print(' '.join(str(x) for x in row))