class Node:
    def __init__(self, summ=0, add=0, replace=-1):
        self.summ = summ
        self.add = add
        self.replace = replace

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [Node() for _ in range(4 * self.n)]
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, v, tl, tr):
        if tl == tr:
            self.tree[v].summ = arr[tl]
        else:
            tm = (tl + tr) // 2
            self.build(arr, v * 2, tl, tm)
            self.build(arr, v * 2 + 1, tm + 1, tr)
            self.tree[v].summ = self.tree[v * 2].summ + self.tree[v * 2 + 1].summ

    def push_tree(self, v, tree_size):
        if self.tree[v].replace != -1:
            if tree_size != 1:
                self.tree[v * 2].replace = self.tree[v].replace
                self.tree[v * 2 + 1].replace = self.tree[v].replace
                self.tree[v * 2].add = 0
                self.tree[v * 2 + 1].add = 0
            self.tree[v].summ = self.tree[v].replace * tree_size
            self.tree[v].replace = -1

        if tree_size != 1:
            self.tree[v * 2].add += self.tree[v].add
            self.tree[v * 2 + 1].add += self.tree[v].add
        self.tree[v].summ += self.tree[v].add * tree_size
        self.tree[v].add = 0

    def get_sum(self, l, r):
        return self.get_sum_util(1, 0, self.n - 1, l, r)

    def get_sum_util(self, v, tl, tr, l, r):
        self.push_tree(v, tr - tl + 1)

        if l > r:
            return 0

        if l == tl and tr == r:
            return self.tree[v].summ

        tm = (tl + tr) // 2
        return self.get_sum_util(v * 2, tl, tm, l, min(r, tm)) + self.get_sum_util(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r)

    def update_replace(self, l, r, value):
        self.update_replace_util(1, 0, self.n - 1, l, r, value)

    def update_replace_util(self, v, tl, tr, l, r, value):
        self.push_tree(v, tr - tl + 1)

        if l > r:
            return

        if l == tl and tr == r:
            self.tree[v].replace = value
            self.push_tree(v, tr - tl + 1)
        else:
            tm = (tl + tr) // 2
            self.update_replace_util(v * 2, tl, tm, l, min(r, tm), value)
            self.update_replace_util(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, value)
            self.tree[v].summ = self.tree[v * 2].summ + self.tree[v * 2 + 1].summ

    def update_add(self, l, r, value):
        self.update_add_util(1, 0, self.n - 1, l, r, value)

    def update_add_util(self, v, tl, tr, l, r, value):
        self.push_tree(v, tr - tl + 1)

        if l > r:
            return

        if l == tl and tr == r:
            self.tree[v].add += value
            self.push_tree(v, tr - tl + 1)
        else:
            tm = (tl + tr) // 2
            self.update_add_util(v * 2, tl, tm, l, min(r, tm), value)
            self.update_add_util(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, value)
            self.tree[v].summ = self.tree[v * 2].summ + self.tree[v * 2 + 1].summ

n, m = map(int, input( ).split())
segment_tree = SegmentTree([0] * n)
for _ in range(m):
    ops = input().split()
    op = int(ops[0])
    if op == 1: segment_tree.update_replace(int(ops[1]), int(ops[2]) - 1, int(ops[3]))
    elif op == 2: segment_tree.update_add(int(ops[1]), int(ops[2]) - 1, int(ops[3]))
    else: print(segment_tree.get_sum(int(ops[1]), int(ops[2]) - 1))

