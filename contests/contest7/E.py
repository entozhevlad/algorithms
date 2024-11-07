a = input()
b = input()
len_a = len(a) + 1
len_b = len(b) + 1
matrix = [[0] * len_b for _ in range(len_a)]

for i in range(len_a):
    matrix[i][0] = i
for j in range(len_b):
    matrix[0][j] = j

for i in range(1, len_a):
    for j in range(1, len_b):
        cost = 0 if a[i - 1] == b[j - 1] else 1
        matrix[i][j] = min(
            matrix[i - 1][j] + 1,
            matrix[i][j - 1] + 1,
            matrix[i - 1][j - 1] + cost
        )
        if i > 1 and j > 1 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
            matrix[i][j] = min(matrix[i][j], matrix[i - 2][j - 2] + cost)
        if i > 1 and j > 1 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
            matrix[i][j] = min(matrix[i][j], matrix[i - 2][j - 2] + 1)

print(matrix[-1][-1])
