class SegmentTree:
    def __init__(self, arr, n):
        self.tree = [0] * (4 * n)
        self.src = arr
        self.build(1, 0, n - 1)

    def build(self, v, tl, tr):
        if tl == tr:
            self.tree[v] = 1 if self.src[tl] == 1 else 0
        else:
            tm = (tl + tr) // 2
            self.build(v * 2, tl, tm)
            self.build(v * 2 + 1, tm + 1, tr)
            self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]

    def get_kth(self, v, tl, tr, k):
        if tl == tr:
            return tl

        tm = (tl + tr) // 2
        if k <= self.tree[v * 2]:
            return self.get_kth(v * 2, tl, tm, k)
        else:
            return self.get_kth(v * 2 + 1, tm + 1, tr, k - self.tree[v * 2])

    def update(self, v, tl, tr, pos):
        if tl == tr:
            self.tree[v] = 0 if self.tree[v] == 1 else 1
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(v * 2, tl, tm, pos)
            else:
                self.update(v * 2 + 1, tm + 1, tr, pos)
            self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
tree = SegmentTree(arr, n)

for _ in range(m):
    op, var = map(int, input().split())
    match op:
        case 1:
            tree.update(1, 0, n - 1, var)
        case 2:
            print(tree.get_kth(1, 0, n - 1, var + 1))
