n = int(input())
dp = [[0] * 3 for _ in range(n)]
dp[0] = [1, 1, 1]
for i in range(1, n):
    dp[i][0] = 2 * dp[i - 1][1]
    dp[i][1] = dp[i][2] = sum(dp[i - 1])
print(sum(dp[-1]))