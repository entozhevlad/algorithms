import sys
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)

    def pop(self):
        top = self.stack.pop()
        return top

stk = Stack()
s = input().split()
for i in s:
    if i.isdigit():
        stk.push(int(i))
    elif i == "+":
        n1 = stk.pop()
        n2 = stk.pop()
        res = (n1 + n2)
        stk.push(res)
    elif i == "-":
        n1 = stk.pop()
        n2 = stk.pop()
        res = (n2 - n1)
        stk.push(res)
    else:
        n1 = stk.pop()
        n2 = stk.pop()
        res = n1 * n2
        stk.push(res)
print(stk.pop())





