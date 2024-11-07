class DS:
    def __init__(self):
        self.S = [0] * 10000
        self.flag = False
        self.x = 0
        self.counter = 0

    def next(self, n):
        minimum = -1
        flag1 = False
        for i in range(self.counter):
            if (not flag1) and (self.S[i] >= n):
                minimum = self.S[i]
                flag1 = True
            elif self.S[i] <= minimum:
                minimum = self.S[i]
        self.flag = True
        self.x = minimum
        print(minimum)

    def add(self, n):
        if self.flag:
            self.S[self.counter] = n + self.x
            self.flag = False
        else:
            self.S[self.counter] = n
        self.counter += 1

A = DS()
k = int(input())
for _ in range(k):
    query, n = input().split()
    n = int(n)
    if query == '+':
        A.add(n)
    else:
        A.next(n)
