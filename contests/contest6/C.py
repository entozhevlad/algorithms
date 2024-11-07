from collections import defaultdict

def is_topsort(n, edges, permutation):
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    position = {}
    for i in range(len(permutation)):
        position[permutation[i]] = i
    for u in range(1, n + 1):
        for v in graph[u]:
            if position[u] > position[v]:
                return "NO"
    return "YES"
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
s = list(map(int, input().split()))
print(is_topsort(n, edges, s))
