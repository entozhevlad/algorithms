import sys
n, m, k = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
prefix_matrix = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix_matrix[i][j] = prefix_matrix[i - 1][j] + prefix_matrix[i][j - 1] - prefix_matrix[i - 1][j - 1] + matrix[i - 1][j - 1]
for _ in range(k):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    if x1 == x2 and y1 == y2:
        sys.stdout.write(str(matrix[y1 - 1][x1 - 1]) + '\n')
    else:
        result = prefix_matrix[y2][x2] - prefix_matrix[y1 - 1][x2] - prefix_matrix[y2][x1 - 1] + prefix_matrix[y1 - 1][x1 - 1]
        sys.stdout.write(str(result) + '\n')



