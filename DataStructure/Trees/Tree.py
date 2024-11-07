### Дерево с корнем в вершине 0
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self, parents, n):
        self.root = TreeNode(0)
        self.nodes = {0: self.root}
        self.depths = {0: 0}
        for i in range(1, n):
            self.nodes[i] = TreeNode(i)
            self.depths[i] = 0
        for i, parent in enumerate(parents):
            self.nodes[parent].children.append(self.nodes[i + 1])

    def height(self, node):
        if not node.children:
            return 0
        return 1 + max(self.height(child) for child in node.children)

    def diameter(self, node=None):
        if node is None:
            node = self.nodes[0]
        max_depth1, max_depth2 = 0, 0
        max_diameter = 0
        for child in node.children:
            depth, diameter = self.diameter(child)
            max_diameter = max(max_diameter, diameter)
            if depth > max_depth1:
                max_depth2 = max_depth1
                max_depth1 = depth
            elif depth > max_depth2:
                max_depth2 = depth
        max_diameter = max(max_diameter, max_depth1 + max_depth2)
        return max_depth1 + 1, max_diameter

    def dfs(self, node=None, depth=0):
        if node is None:
            node = self.root
        self.depths[node.value] = depth
        for child in node.children:
            self.dfs(child, depth + 1)

        return self.depths