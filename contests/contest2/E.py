import sys
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if self.stack:
            return self.stack.pop()
    def last(self):
        if self.stack:
            return self.stack[-1]
n = int(sys.stdin.readline())
way1 = list(map(int, sys.stdin.readline().split()))
end = Stack()
idx = 0
cur = 1
way2 = 0
result = []
flag = True
while way2 != n:
    count = 0
    while cur not in end.stack:
        end.push(way1[idx])
        idx += 1
        count +=1
    result.append((1,count))
    count = 0
    while end and end.last() == cur:
        end.pop()
        cur += 1
        way2+=1
        count += 1
    if end.stack and end.last() > cur and cur in end.stack:
        flag = False
        break
    result.append((2,count))
if flag:
    sys.stdout.write(str(len(result)) + '\n')
    for i in result:
        sys.stdout.write(' '.join(map(str, i)) + '\n')
else:
    sys.stdout.write(str(0))









