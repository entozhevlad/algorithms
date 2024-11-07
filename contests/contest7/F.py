n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
for i in range(n):
    dp[i][0] = matrix[i][0]
for j in range(m):
    dp[0][j] = matrix[0][j]

for i in range(1, n):
    for j in range(1, m):
        if matrix[i][j] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

max_side = max(max(row) for row in dp)

top_x = top_y = 0
for i in range(n):
    for j in range(m):
        if dp[i][j] == max_side:
            top_x = i - max_side + 1
            top_y = j - max_side + 1
            break

print(max_side)
print(top_x + 1, top_y + 1)
