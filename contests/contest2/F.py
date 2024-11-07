import sys
from collections import deque
n = int(sys.stdin.readline())
deq = deque()
pos = {}
left = 0
for _ in range(n):
    event = list(map(int, sys.stdin.readline().split()))
    match event[0]:
        case 1:
            el = event[1]
            deq.append(el)
            pos[el] = len(deq) - 1 + left
        case 2:
            el = deq.popleft()
            left += 1
        case 3:
            deq.pop()
        case 4:
            sys.stdout.write(str(pos[event[1]] - left) + '\n')
        case 5:
            sys.stdout.write(str(deq[0]) + '\n')
