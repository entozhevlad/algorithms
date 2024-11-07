from collections import deque
def knightDistance(N, x1, y1, x2, y2):
    vertices = []
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            vertices.append((i, j))
    moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, -1), (-2, 1)]
    edges = {}
    for (i, j) in vertices:
        if (i, j) not in edges.keys():
            edges[(i, j)] = []
        for (dx, dy) in moves:
            nx = i + dx
            ny = j + dy
            if nx >= 1 and nx <= N and ny >= 1 and ny <= N:
                edges[(i, j)].append((nx, ny))

    q = deque()
    visited = set()
    parent = {}
    parent[(x1, y1)] = None
    q.append((x1, y1))
    visited.add((x1, y1))
    while len(q) > 0:
        u = q.popleft()
        if u == (x2, y2):
            path = []
            while u is not None:
                path.append(u)
                u = parent[u]
            path = path[::-1]
            return len(path) - 1, path
        for t in edges[u]:
            if t in visited:
                continue
            q.append(t)
            visited.add(t)
            parent[t] = u


n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
steps, path = knightDistance(n, x1, y1, x2, y2)
print(steps)
for coord in path:
    print(coord[0], coord[1])