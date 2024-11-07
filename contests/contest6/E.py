import heapq
k = int(input())
graph = [[] for _ in range(10**5)]
for i in range(1, k + 1):
    start, end = i % k, (i + 1) % k
    graph[start].append((end, 1))
for i in range(1, k + 1):
    start, end = i % k, (10 * i) % k
    graph[start].append((end, 0))
queue = [(0, 1)]
root = 1
distance = [float('inf')] * (k + 2)
heapq.heappush(queue, (0, root))
distance[root] = 0
while queue:
    cur_dist, cur = heapq.heappop(queue)
    for v, weight in graph[cur]:
        if distance[v] > distance[cur] + weight:
            distance[v] = distance[cur] + weight
            heapq.heappush(queue, (distance[v], v))
print(1 + distance[0])

