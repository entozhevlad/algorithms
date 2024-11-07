def check_slices(arr, n, final):
    slices, summ = 1, 0
    for i in range(n):
        summ += arr[i]
        if summ > final:
            slices += 1
            summ = arr[i]
    return slices
n, k = map(int, input().split())
arr = list(map(int, input().split()))
l, r  = max(arr), sum(arr)
while l < r:
    m = (l + r) // 2
    if check_slices(arr, n, m) <= k:
        r = m
    else:
        l = m + 1
print(l)
