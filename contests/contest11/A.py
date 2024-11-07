import sys
sys.setrecursionlimit(100000)
class TreeNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.children = []

class Tree:
    def __init__(self, n, parents):
        self.root = TreeNode(0)
        self.nodes = {0: self.root}
        self.depths = {}
        for i in range(1, n):
            self.nodes[i] = TreeNode(i)
            self.depths[i] = 0
        for i, parent in enumerate(parents):
            parent = self.nodes[parent]
            child = self.nodes[i + 1]
            child.parent = parent
            parent.children.append(child)
        self.dfs()

    def dfs(self, node=None, depth=0):
        if node is None:
            node = self.root
        self.depths[node.value] = depth
        for child in node.children:
            self.dfs(child, depth + 1)
        return self.depths


    def lca(self, u, v):
        while u.value != v.value:
            if self.depths[u.value] < self.depths[v.value]:
                v = v.parent
            elif self.depths[u.value] > self.depths[v.value]:
                u = u.parent
            else:
                u, v = u.parent, v.parent
        return u.value


n = int(input())
parents = list(map(int, input().split()))
tree = Tree(n, parents)
m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    print(tree.lca(tree.nodes[u], tree.nodes[v]))