import sys
n, k = map(int, sys.stdin.readline().split())
l, r = 1, n ** 2
while l < r:
    m = (l + r) // 2
    count = sum(min(m // i, n) for i in range(1, n + 1))
    if count < k:
        l = m + 1
    else:
        r = m
sys.stdout.write(str(l) + '\n')