def dfs(self, node, result):
    if node is None:
        return
    if node is not None:
        if node.left is None and node.right is None:
            result.append(node.value)
    left_node = self.dfs(node.left, result)
    right_node = self.dfs(node.right, result)