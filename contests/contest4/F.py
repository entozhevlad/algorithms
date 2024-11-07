import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    l, r = map(int, sys.stdin.readline().split())
    arr.append((l, r))
arr.sort()
length, cur_start, cur_end = 0, None, None
for start, end in arr:
    if cur_start is None:
        cur_start, cur_end = start, end
    elif start <= cur_end:
        cur_end = max(cur_end, end)
    else:
        length += cur_end - cur_start
        cur_start, cur_end = start, end
if cur_start is not None:
    length += cur_end - cur_start
sys.stdout.write(str(length) + '\n')