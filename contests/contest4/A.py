import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sums = [arr[0]] + [0] * (n - 1)
xors = [arr[0]] + [0] * (n - 1)
for i in range(1, n):
    sums[i] = sums[i - 1] + arr[i]
    xors[i] = xors[i - 1] ^ arr[i]
m = int(sys.stdin.readline())
for _ in range(m):
    q, l, r = map(int, sys.stdin.readline().split())
    if q == 1:
        sys.stdout.write(str(sums[r - 1] - sums[l - 1] + arr[l - 1]) + '\n')
    elif q == 2:
        sys.stdout.write(str(xors[r - 1] ^ xors[l - 1] ^ arr[l - 1]) + '\n')
