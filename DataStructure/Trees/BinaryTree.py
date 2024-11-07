class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class SimpleTree:
    def __init__(self):
        self.root = TreeNode()

    def add(self, value):
        if self.root.value is None:
            self.root.value = value
        else:
            cur = self.root
            while True:
                if cur.value > value:
                    if cur.left is None:
                        cur.left = TreeNode(value)
                        break
                    else:
                        cur = cur.left
                elif cur.value < value:
                    if cur.right is None:
                        cur.right = TreeNode(value)
                        break
                    else:
                        cur = cur.right
                else:
                    break

    def hasValue(self, value):
        cur = self.root
        if cur.value is None:
            return False
        while cur is not None:
            if cur.value > value:
                cur = cur.left
            elif cur.value < value:
                cur = cur.right
            else:
                return True
        return False