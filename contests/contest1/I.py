n = int(input())
arr = [0] * n
indexes = list(map(int, input().split()))
count, last = 0, 0
idx = n - 1
result = [1]
for i in range(n - 1):
    arr[indexes[i] - 1] = 1
    count += 1
    if arr[idx] == 0:
        result.append(count + 1 - last)
    else:
        while arr[idx] == 1:
            last += 1
            idx -= 1
        result.append(count + 1 - last)
result.append(1)
print(*result)
