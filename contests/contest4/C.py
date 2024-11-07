n, k = map(int, input().split())
arr = list(map(int, input().split()))
def checker(arr, k, distance):
    count = 1
    last = arr[0]
    for st in arr:
        if st - last >= distance:
            count += 1
            last = st
    return count >= k
def bin_search(arr, k, n):
    l, r = 0, arr[n-1] - arr[0]
    maximum = 0
    while l <= r:
        m = (l + r) // 2
        if checker(arr, k, m):
            maximum = m
            l = m + 1
        else:
            r = m - 1
    print(maximum)

bin_search(arr, k, n)