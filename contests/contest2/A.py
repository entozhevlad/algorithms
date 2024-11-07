import sys
class Stack:
    def __init__(self):
        self.stack = []
        self.mins = []
    def push(self, x):
        self.stack.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)
    def pop(self):
        top = self.stack.pop()
        if top == self.mins[-1]:
            self.mins.pop()
    def minimum(self):
        sys.stdout.write(str(self.mins[-1]) + '\n')

n = int(sys.stdin.readline())
stk = Stack()
for _ in range(n):
    op = sys.stdin.readline().strip().split()
    match op[0]:
        case "1": stk.push(int(op[1]))
        case "2": stk.pop()
        case "3": stk.minimum()





