class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, x):
        self.heap.append(x)
        idx = len(self.heap) - 1
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent
            else:
                break

    def extract(self):
        minimum = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        idx = 0
        n = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            m_child = idx
            if left < n and self.heap[left] < self.heap[m_child]:
                m_child = left
            if right < n and self.heap[right] < self.heap[m_child]:
                m_child = right
            if m_child == idx:
                break
            self.heap[idx], self.heap[m_child] = self.heap[m_child], self.heap[idx]
            idx = m_child
        return minimum

    def sort(self):
        sorted_list = []
        while self.heap:
            sorted_list.append(self.extract())
        return sorted_list

n = int(input())
numbers = list(map(int, input().split()))
heap = Heap()
for num in numbers:
    heap.insert(num)
print(*heap.sort())