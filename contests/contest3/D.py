class Heap:
    def __init__(self):
        self.heap = []
    def insert(self, x):
        self.heap.append(x)
        idx = len(self.heap) - 1
        while idx > 0:
            parent = (idx - 1)//2
            if self.heap[idx] > self.heap[parent]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent
            else:
                break
    def extract(self):
        maximum = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        idx = 0
        n = len(self.heap)
        while 2*idx + 1 < n:
            left = 2 * idx + 1
            right = 2 * idx + 2 if 2 * idx + 2 < n else None
            m_child = left
            if right is not None and self.heap[right] > self.heap[left]:
                m_child = right
            if self.heap[idx] < self.heap[m_child]:
                self.heap[idx], self.heap[m_child] = self.heap[m_child], self.heap[idx]
                idx = m_child
            else:
                break
        return maximum

n = int(input())
heap = Heap()
for _ in range(n):
    s = list(map(int, input().split()))
    match s[0]:
        case 0: heap.insert(s[1])
        case 1: print(heap.extract())
