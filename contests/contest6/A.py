import sys
sys.setrecursionlimit(1000000)
class Graph:
    def __init__(self, n):
        self.graph = {i : [] for i in range(1, n+1)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, vertex, visited, component):
        visited[vertex] = True
        component.append(vertex)
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, component)

    def connected_components(self):
        visited = {vertex: False for vertex in self.graph}
        components = []
        for vertex in self.graph:
            if not visited[vertex]:
                component = []
                self.dfs(vertex, visited, component)
                components.append(component)
        return components

n,m = map(int, input().split())
graph = Graph(n)
for _ in range(m):
    i, j = map(int, input().split())
    graph.add_edge(i, j)
result = graph.connected_components()
print(len(result))
for component in result:
    print(len(component))
    print(*sorted(component))


