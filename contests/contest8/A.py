class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.build(arr)

    def build(self, arr):
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[(i * 2)] + self.tree[(i * 2) + 1]

    def update(self, p, value):
        p += self.n
        self.tree[p] = value
        while p > 1:
            parent = p // 2
            self.tree[parent] = self.tree[p] + self.tree[p ^ 1]
            p = parent

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l % 2:
                res += self.tree[l]
                l += 1
            if r % 2:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res

n, m = map(int, input().split())
a = list(map(int, input().split()))
segment_tree = SegmentTree(a)
for _ in range(m):
    op, i, v = map(int, input().split())
    if op == 1:
        segment_tree.update(i, v)
    elif op == 2:
        print(segment_tree.query(i, v))
