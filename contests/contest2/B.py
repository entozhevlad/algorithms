from collections import deque
import sys
n, k = map(int, input().split())
s = list(map(int, input().split()))
deq = deque()
for i in range(n):
    while deq and s[deq[-1]] >= s[i]:
        deq.pop()
    deq.append(i)
    if i - deq[0] >= k:
        deq.popleft()
    if i >= k - 1:
        sys.stdout.write(str(s[deq[0]]) + ' ')



