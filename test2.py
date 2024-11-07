s = input()
n = len(s)
dp = [[float('inf')] * (n + 1) for i in range(n + 1)]
best = [[-1] * (n + 1) for i in range(n + 1)]
for i in range(n + 1):
    dp[i][i] = 1
for i in range(n - 1):
    if (s[i] == '(' and s[i + 1] == ')') or (s[i] == '[' and s[i + 1] == ']') or (s[i] == '{' and s[i + 1] == '}'):
        dp[i][i + 1] = 0
for L in range(2, n + 1):
    for left in range(n - L + 1):
        right = left + L - 1
        if (s[left] == '(' and s[right] == ')') or (s[left] == '[' and s[right] == ']') or (s[left] == '{' and s[right] == '}'):
            dp[left][right] = min(dp[left] [right], dp[left + 1] [right - 1])
        for mid in range(left, right):
            cur = dp[left][mid] + dp[mid + 1][right]
            if dp[left][right] > cur:
                dp[left][right] = cur
                best[left][right] = mid

print(dp[0][n - 1])