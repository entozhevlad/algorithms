def floyd_warshall(graph, n):
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for u, v, w in graph:
        dist[u - 1][v - 1] = w
        dist[v - 1][u - 1] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    min_dist = float('inf')
    result = -1

    for i in range(n):
        max_dist = max(dist[i])
        if max_dist < min_dist:
            min_dist = max_dist
            result = i + 1

    return result


n, m = map(int, input().split())
graph = []
for _ in range(m):
    data = list(map(int, input().split()))
    graph.append(data)
result = floyd_warshall(graph, n)
print(result)
