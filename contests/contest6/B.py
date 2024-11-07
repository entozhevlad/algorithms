import sys
sys.setrecursionlimit(1000000)
class Graph:
    def __init__(self, n):
        self.graph = {i : [] for i in range(1,n+1)}

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def find_cycle(self):
        visited = {vertex: False for vertex in self.graph}
        stack = []

        def dfs(vertex, start):
            visited[vertex] = True
            stack.append(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor == start:
                    return True
                if not visited[neighbor]:
                    if dfs(neighbor, start):
                        return True
                elif neighbor in stack:
                    return True
            stack.pop()
            return False

        for vertex in self.graph:
            if not visited[vertex]:
                if dfs(vertex, vertex):
                    return True
        return False


n, m = map(int, input().split())
graph = Graph(n)
for _ in range(m):
    u, v = map(int, input().split())
    graph.add_edge(u, v)
if graph.find_cycle():
    print(1)
else:
    print(0)
