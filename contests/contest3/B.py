import sys
sys.setrecursionlimit(1000000)
class TreeNode:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self,n, r):
        self.nodes = [TreeNode(i) for i in range(n)]
        self.root = self.nodes[r]
    def isAVL(self, root, minimum=float('-inf'), maximum=float('inf')):
        if root is None:
            return True, True, 0
        l_balanced, l_bst, l_h = self.isAVL(root.left, minimum, root.value)
        if not l_balanced or not l_bst:
            return False, False, 0
        r_balanced, r_bst, r_h = self.isAVL(root.right, root.value, maximum)
        if not r_balanced or not r_bst:
            return False, False, 0
        balance = abs(l_h - r_h) <= 1
        bst = root.value > minimum and root.value < maximum
        h = max(l_h, r_h) + 1
        return balance, bst, h


n, r = map(int, input().split())
tree = BinaryTree(n, r)
for i in range (n):
    l, r = map(int, input().split())
    if l != -1:
        tree.nodes[i].left = tree.nodes[l]
    if r != -1:
        tree.nodes[i].right = tree.nodes[r]

if tree.isAVL(tree.root)[0]:
    print(1)
else:
    print(0)
