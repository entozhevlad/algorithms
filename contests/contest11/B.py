import sys

def build(graph, depth, dp, max_i, max_depth, v, p = 0, c = sys.maxsize):
    if p != v:
        depth[v] = depth[p] + 1

    dp[v][0] = (p, c)
    for i in range(1, max_i + 1):
        dp[v][i] = (dp[dp[v][i - 1][0]][i - 1][0], min(dp[v][i - 1][1], dp[dp[v][i - 1][0]][i - 1][1]))

    for next_v, cost in graph[v]:
        build(graph, depth, dp, max_i, max_depth, next_v, v, cost)

def min_lca(depth, dp, max_i, u, v):
    res = sys.maxsize

    if depth[v] > depth[u]:
        u, v = v, u

    for i in range(max_i, -1, -1):
        if depth[dp[u][i][0]] >= depth[v]:
            res = min(res, dp[u][i][1])
            u = dp[u][i][0]

    if v == u:
        return res

    for i in range(max_i, -1, -1):
        if dp[v][i][0] != dp[u][i][0]:
            res = min(res, dp[v][i][1])
            v = dp[v][i][0]
            res = min(res, dp[u][i][1])
            u = dp[u][i][0]

    res = min(res, dp[u][0][1])
    res = min(res, dp[v][0][1])

    return res

n = int(input())

graph = [[] for _ in range(n)]
for i in range(1, n):
    x, y = map(int, input().split())
    x += 1
    y += 1
    graph[x - 1].append((i, y))

depth = [0] * n
max_i = 1
while (1 << max_i) <= n:
    max_i += 1

dp = [[(0, 0)] * (max_i + 1) for _ in range(n)]
build(graph, depth, dp, max_i, n, 0)

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    u += 1
    v += 1
    print(min_lca(depth, dp, max_i, u - 1, v - 1) - 1)
