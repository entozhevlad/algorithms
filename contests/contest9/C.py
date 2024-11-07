class SegmentTree:
    class Node:
        def __init__(self, n=1, seg=1, s=0, left=0, right=0, u=False):
            self.number = n
            self.segments = seg
            self.set = s
            self.l = left
            self.r = right
            self.up = u

    def __init__(self, n):
        self.t = [self.Node() for _ in range(4 * n)]

    def build(self, v, tl, tr):
        if tl == tr:
            self.t[v] = self.Node(0, 0, 0, tl, tr, False)
        else:
            tm = self.get_middle(tl, tr)
            self.build(v * 2, tl, tm)
            self.build(v * 2 + 1, tm + 1, tr)
            self.t[v] = self.Node(0, 0, 0, tl, tr, False)

    def push(self, v):
        if not self.t[v].up:
            return

        self.t[v].number = self.t[v].set * (self.t[v].r - self.t[v].l + 1)
        self.t[v].segments = 1 * self.t[v].set
        self.t[v].up = False

        if self.t[v].l == self.t[v].r:
            return

        self.t[v * 2].set = self.t[v].set
        self.t[v * 2 + 1].set = self.t[v].set

        self.t[v * 2].up = True
        self.t[v * 2 + 1].up = True

    def left_is_black(self, v):
        self.push(v)

        if self.t[v].l == self.t[v].r:
            return self.t[v].number == 1

        return self.left_is_black(v * 2)

    def right_is_black(self, v):
        self.push(v)

        if self.t[v].l == self.t[v].r:
            return self.t[v].number == 1

        return self.right_is_black(v * 2 + 1)

    def update(self, v, value, l, r):
        if self.t[v].r < l or self.t[v].l > r:
            return

        if self.t[v].r <= r and self.t[v].l >= l:
            self.push(v)
            self.t[v].set = value
            self.t[v].up = True
            return

        self.push(v)
        self.update(v * 2, value, l, r)
        self.update(v * 2 + 1, value, l, r)

        left = self.right_is_black(v * 2)
        right = self.left_is_black(v * 2 + 1)

        self.t[v].number = self.t[v * 2].number + self.t[v * 2 + 1].number
        self.t[v].segments = self.t[v * 2 + 1].segments + self.t[v * 2].segments

        if left and right:
            self.t[v].segments -= 1

    def get_middle(self, l, r):
        return l + (r - l) // 2

n = int(input())
color, cord, delta = [],[],[]
maxdelta = 0
maxcord, mincord = float("-inf"), float("inf")

for _ in range(n):
    c, c_ord, d = input().split()
    c_ord, d = int(c_ord), int(d)
    if d > 0:
        d -= 1
    else:
        d += 1

    del_ = c_ord + d
    if del_ > maxcord:
        maxcord = del_
    if maxdelta > c_ord:
        maxdelta = c_ord
    color.append(c)
    cord.append(c_ord)
    delta.append(d)

length = maxcord - maxdelta + 1 + abs(maxdelta)  # Скорректируйте длину, чтобы учесть отрицательные индексы
segment_tree = SegmentTree(length)
segment_tree.build(1, 0, length)

for i in range(n):
    if color[i] == 'W':
        segment_tree.update(1, 0, cord[i] + abs(maxdelta) - maxdelta, cord[i] + delta[i] + abs(maxdelta) - maxdelta)  # Скорректируйте индексы
        print(segment_tree.t[1].segments, segment_tree.t[1].number)
    else:
        segment_tree.update(1, 1, cord[i] + abs(maxdelta) - maxdelta, cord[i] + delta[i] + abs(maxdelta) - maxdelta)  # Скорректируйте индексы
        print(segment_tree.t[1].segments, segment_tree.t[1].number)

