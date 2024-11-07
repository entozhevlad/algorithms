n, k = map(int,input().split())
def bin_search(arr,target):
    l,r = 0, len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            return "YES"
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return "NO"

arr = list(map(int,input().split()))
targets = list(map(int,input().split()))
for target in targets:
    print(bin_search(arr,target))