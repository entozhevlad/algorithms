import heapq

def prim(graph, n):
    visited = [False] * n
    min_heap = [(0, 0)]
    min_spanning_tree_weight = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if not visited[node]:
            visited[node] = True
            min_spanning_tree_weight += weight

            for neighbor, edge_weight in graph[node]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (edge_weight, neighbor))

    return min_spanning_tree_weight

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    b, e, w = map(int, input().split())
    graph[b - 1].append((e - 1, w))
    graph[e - 1].append((b - 1, w))
print(prim(graph,n))
