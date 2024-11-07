import heapq

def dijkstra(graph, src):
    n = len(graph)
    dist = [float('inf')] * n
    dist[src] = 0
    min_heap = [(0, src)]  # (расстояние, вершина)
    while min_heap:
        curr_dist, curr_node = heapq.heappop(min_heap)

        if curr_dist > dist[curr_node]:
            continue

        for neighbor, weight in graph[curr_node]:
            new_dist = curr_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    return dist

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    start, end, weight = map(int, input().split())
    graph[start - 1].append((end - 1, weight))
    graph[end - 1].append((start - 1, weight))

print(*dijkstra(graph, 0))
