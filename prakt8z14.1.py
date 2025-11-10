n = int(input())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

m = int(input())

max_index = 0
for i in range(1, n):
    if matrix[i][i] > matrix[max_index][max_index]:
        max_index = i

if max_index != m - 1:
    matrix[max_index], matrix[m - 1] = matrix[m - 1], matrix[max_index]

for row in matrix:
    print(' '.join(map(str, row)))