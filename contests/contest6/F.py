import heapq

def dijkstra(graph, start, end):
    if start not in graph or end not in graph:
        return -1

    dist = {edge: float('inf') for edge in graph}
    dist[start] = 0

    queue = [(0, start)]

    while queue:
        curr_dist, curr_edge = heapq.heappop(queue)
        if curr_dist > dist[curr_edge]:
            continue

        for edge in graph[curr_edge]:
            weight = 1
            distance = curr_dist + weight

            if distance < dist[edge]:
                dist[edge] = distance
                heapq.heappush(queue, (distance, edge))

    return dist[end] if dist[end] != float('inf') else -1



n = int(input())
graph = {}
for _ in range(n):
    s = input().split(' -> ')
    if s[0] in graph:
        graph[s[0]].append(s[1])
    else:
        graph[s[0]] = [s[1]]
    if s[1] not in graph:
        graph[s[1]] = []
start = input()
end = input()
print(dijkstra(graph, start, end))

