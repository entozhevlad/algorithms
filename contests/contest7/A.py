n = int(input())
arr = list(map(int, input().split()))
if n < 3:
    print(arr[-1])
else:
    dp = [0 for i in range(n)]
    dp[0], dp[1] = arr[0], arr[1]
    for i in range(2, n):
        dp[i] = min(arr[i] + dp[i-1], arr[i] + dp[i-2])
    print(dp[-1])
