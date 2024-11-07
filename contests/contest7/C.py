from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().split())
coins = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[1] = 0
queue = deque()
queue.append(1)
prev = [-1] * (n + 1)

for i in range(2, n + 1):
    while queue and queue[0] < i - k:
        queue.popleft()
    dp[i] = dp[queue[0]] + (coins[i - 2] if i != n else 0)
    prev[i] = queue[0]

    while queue and dp[i] >= dp[queue[-1]]:
        queue.pop()
    queue.append(i)

path = []
curr = n
while curr != -1:
    path.append(curr)
    curr = prev[curr]
path = path[::-1]
print(str(dp[-1]) + '\n')
print(str(len(path) - 1) + '\n')
print(' '.join(map(str, path)))
