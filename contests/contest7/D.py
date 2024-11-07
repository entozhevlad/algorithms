def knight_steps(i, j):
    if (i >= 0) and (j >= 0) and (i < n) and (j < m):
        if dp[i][j] == -1:
            dp[i][j] = knight_steps(i - 2, j - 1) + knight_steps(i - 2, j + 1) + knight_steps(i - 1, j - 2) + knight_steps(i + 1, j - 2)
    else:
        return 0
    return dp[i][j]
n, m = map(int, input().split())
dp = [[-1] * m for _ in range(n)]
dp[0][0] = 1
print(knight_steps(n - 1, m - 1))