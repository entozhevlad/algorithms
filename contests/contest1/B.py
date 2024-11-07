def bin_search(arr, target):
    l,r = 0, len(arr)-1
    ans = [float('inf'), float('inf')]
    while l <= r:
        m = (l+r)//2
        tmp = arr[m] - target
        dif = abs(tmp)
        if dif < ans[0] or (dif == ans[0] and arr[m] < ans[1]):
            ans = [dif, arr[m]]
        if dif == 0:
            return arr[m]
        elif tmp < 0:
            l = m + 1
        else:
            r = m - 1
    return ans[1]

n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
for i in arr2:
    print(bin_search(arr1, i))
