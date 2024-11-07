class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.min_element = list(range(n + 1))
        self.max_element = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
            self.min_element[y_root] = min(self.min_element[y_root], self.min_element[x_root])
            self.max_element[y_root] = max(self.max_element[y_root], self.max_element[x_root])
            self.size[y_root] += self.size[x_root]
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
            self.min_element[x_root] = min(self.min_element[x_root], self.min_element[y_root])
            self.max_element[x_root] = max(self.max_element[x_root], self.max_element[y_root])
            self.size[x_root] += self.size[y_root]
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
            self.min_element[x_root] = min(self.min_element[x_root], self.min_element[y_root])
            self.max_element[x_root] = max(self.max_element[x_root], self.max_element[y_root])
            self.size[x_root] += self.size[y_root]

    def get(self, x):
        root = self.find(x)
        return self.min_element[root], self.max_element[root], self.size[root]

n, m = map(int, input().split())
structure = DisjointSet(n)
for _ in range(m):
    query = input().split()
    if query[0] == 'union':
        x, y = map(int, query[1:])
        structure.union(x, y)
    else:
        x = int(query[1])
        minn, maxx, size = structure.get(x)
        print(minn, maxx, size)
