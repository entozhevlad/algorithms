class SegmentTree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.min_tree = [0] * (2 * self.size - 1)
        self.lazy = [0] * (2 * self.size - 1)

    def _propagate(self, v, l, r):
        if self.lazy[v] != 0:
            self.min_tree[v] += self.lazy[v]
            if r - l > 1:
                self.lazy[2*v+1] += self.lazy[v]
                self.lazy[2*v+2] += self.lazy[v]
            self.lazy[v] = 0

    def _add(self, v, l, r, ql, qr, val):
        self._propagate(v, l, r)
        if qr <= l or r <= ql:
            return
        if ql <= l and r <= qr:
            self.lazy[v] += val
            self._propagate(v, l, r)
            return
        mid = (l + r) // 2
        self._add(2*v+1, l, mid, ql, qr, val)
        self._add(2*v+2, mid, r, ql, qr, val)
        self.min_tree[v] = min(self.min_tree[2*v+1] + self.lazy[2*v+1], self.min_tree[2*v+2] + self.lazy[2*v+2])

    def _query(self, v, l, r, ql, qr):
        self._propagate(v, l, r)
        if qr <= l or r <= ql:
            return float('inf')
        if ql <= l and r <= qr:
            return self.min_tree[v]
        mid = (l + r) // 2
        left_min = self._query(2*v+1, l, mid, ql, qr)
        right_min = self._query(2*v+2, mid, r, ql, qr)
        return min(left_min, right_min)

    def add(self, l, r, val):
        self._add(0, 0, self.size, l, r, val)

    def query(self, l, r):
        return self._query(0, 0, self.size, l, r)


n, m = map(int, input().split())
tree = SegmentTree(n)

for _ in range(m):
    op = input().split()
    if op[0] == '1':
        l, r, v = map(int, op[1:])
        tree.add(l, r, v)
    elif op[0] == '2':
        l, r = map(int, op[1:])
        print(tree.query(l, r))
