class Stack:
    def __init__(self):
        self.stack = []
        self.count = 0

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        top = self.stack.pop()
        self.count += 1
        return top


n = int(input())
balls = list(map(int, input().split()))
stk = Stack()
for i in range(n):
    ball = balls[i]
    if len(stk.stack) >= 3:
        lst = set(stk.stack[-3:])
        if len(lst) == 1:
            if ball in stk.stack[-3:]:
                stk.push(ball)
                if i == n - 1:
                    while stk.stack and stk.stack[-1] in lst:
                        stk.pop()
                    break
                else:
                    continue
            else:
                while stk.stack[-1] in lst and len(stk.stack) > 0:
                    stk.pop()
        else:
            stk.push(ball)
            continue
    stk.push(ball)
print(stk.count)