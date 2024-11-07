class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self, parents):
        self.nodes = [TreeNode(value) if value is not None else None for value in parents]
        self.root = self.nodes[0] if self.nodes else None
        self.result = []
        for i in range(len(self.nodes)):
            node = self.nodes[i]
            if node is not None:
                left_index = 2 * i + 1
                right_index = 2 * i + 2
                if left_index < len(self.nodes):
                    node.left = self.nodes[left_index]
                if right_index < len(self.nodes):
                    node.right = self.nodes[right_index]

    def dfs(self, node, result):
        if node is None:
            return
        if node is not None:
            if node.left is None and node.right is None:
                result.append(node.value)
        left_node = self.dfs(node.left, result)
        right_node = self.dfs(node.right, result)


# Пример использования
root1 = [1,2,3]
root2 = [1,3,2]
a = Tree(root1)
b = Tree(root2)
a.dfs(a.root, a.result)
b.dfs(b.root, b.result)
print(a.result == b.result)