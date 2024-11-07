class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree_sum = [0] * (2 * self.n)
        self.tree_min = [float('inf')] * (2 * self.n)
        self.tree_min_count = [0] * (2 * self.n)
        self.build(arr)

    def build(self, arr):
        for i in range(self.n):
            self.tree_sum[self.n + i] = arr[i]
            self.tree_min[self.n + i] = arr[i]
            self.tree_min_count[self.n + i] = 1
        for i in range(self.n - 1, 0, -1):
            self.tree_sum[i] = self.tree_sum[i * 2] + self.tree_sum[i * 2 + 1]
            if self.tree_min[i * 2] < self.tree_min[i * 2 + 1]:
                self.tree_min[i] = self.tree_min[i * 2]
                self.tree_min_count[i] = self.tree_min_count[i * 2]
            elif self.tree_min[i * 2] > self.tree_min[i * 2 + 1]:
                self.tree_min[i] = self.tree_min[i * 2 + 1]
                self.tree_min_count[i] = self.tree_min_count[i * 2 + 1]
            else:
                self.tree_min[i] = self.tree_min[i * 2]
                self.tree_min_count[i] = self.tree_min_count[i * 2] + self.tree_min_count[i * 2 + 1]

    def update(self, p, value):
        p += self.n
        self.tree_sum[p] = value
        self.tree_min[p] = value
        self.tree_min_count[p] = 1
        while p > 1:
            parent = p // 2
            self.tree_sum[parent] = self.tree_sum[p] + self.tree_sum[p ^ 1]
            if self.tree_min[p] < self.tree_min[p ^ 1]:
                self.tree_min[parent] = self.tree_min[p]
                self.tree_min_count[parent] = self.tree_min_count[p]
            elif self.tree_min[p] > self.tree_min[p ^ 1]:
                self.tree_min[parent] = self.tree_min[p ^ 1]
                self.tree_min_count[parent] = self.tree_min_count[p ^ 1]
            else:
                self.tree_min[parent] = self.tree_min[p]
                self.tree_min_count[parent] = self.tree_min_count[p] + self.tree_min_count[p ^ 1]
            p = parent

    def query(self, l, r):
        min_val = float('inf')
        min_count = 0
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l % 2:
                res += self.tree_sum[l]
                if self.tree_min[l] < min_val:
                    min_val = self.tree_min[l]
                    min_count = self.tree_min_count[l]
                elif self.tree_min[l] == min_val:
                    min_count += self.tree_min_count[l]
                l += 1
            if r % 2:
                r -= 1
                res += self.tree_sum[r]
                if self.tree_min[r] < min_val:
                    min_val = self.tree_min[r]
                    min_count = self.tree_min_count[r]
                elif self.tree_min[r] == min_val:
                    min_count += self.tree_min_count[r]
            l //= 2
            r //= 2
        return min_val, min_count

n, m = map(int, input().split())
a = list(map(int, input().split()))
segment_tree = SegmentTree(a)
for _ in range(m):
    op, i, v = map(int, input().split())
    if op == 1:
        segment_tree.update(i, v)
    elif op == 2:
        min_val, count_min = segment_tree.query(i, v)
        print(min_val, count_min)
