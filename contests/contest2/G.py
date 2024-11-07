from collections import deque
import sys
n = int(sys.stdin.readline())
deq1, deq2 = deque(), deque()
for _ in range(n):
    goblin = sys.stdin.readline().split()
    match goblin[0]:
        case "+":
            deq1.appendleft(goblin[1])
        case "*":
            while len(deq1) > len(deq2):
                deq2.appendleft(deq1.pop())
            deq1.append(goblin[1])
        case "-":
            while len(deq1) > len(deq2):
                deq2.appendleft(deq1.pop())
            sys.stdout.write(str(deq2.pop()) + '\n')







