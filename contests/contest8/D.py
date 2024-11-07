class SegmentTree:
    def __init__(self, a, n):
        self.tree = [0] * (4 * n)
        self.build(a, 1, 0, n - 1)

    def build(self, a, v, tl, tr):
        if tl == tr:
            self.tree[v] = a[tl]
        else:
            tm = (tl + tr) // 2
            self.build(a, v * 2, tl, tm)
            self.build(a, v * 2 + 1, tm + 1, tr)
            self.tree[v] = max(self.tree[v * 2], self.tree[v * 2 + 1])

    def get_gex(self, v, tl, tr, l, r, x):
        if l > r:
            return float('inf')

        if tl == tr:
            return tl if self.tree[v] >= x else float('inf')

        tm = (tl + tr) // 2

        if tl < l:
            return min(
                self.get_gex(v * 2, tl, tm, l, min(r, tm), x),
                self.get_gex(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, x)
            )
        else:
            if self.tree[v * 2] >= x:
                return self.get_gex(v * 2, tl, tm, l, min(r, tm), x)
            else:
                return self.get_gex(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, x)

    def update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(v * 2, tl, tm, pos, new_val)
            else:
                self.update(v * 2 + 1, tm + 1, tr, pos, new_val)
            self.tree[v] = max(self.tree[v * 2], self.tree[v * 2 + 1])


n, m = map(int, input().split())
arr = list(map(int, input().split()))

tree = SegmentTree(arr)

for _ in range(m):
    op, i, v = map(int, input().split())
    if op == 1:
        tree.update(1, 0, n - 1, i, v)
    else:
        res = tree.get_gex(1, 0, n - 1, v, n - 1, i)
        print(-1 if res == float('inf') else res)
