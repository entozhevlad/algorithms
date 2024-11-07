import sys
n = int(input())
def query(x):
    print(x)
    sys.stdout.flush()
    return input()

s = list(range(1,n+1))
def bin_search(arr):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l + r) // 2
        x = arr[mid]
        if query(x) == "<":
            r = mid - 1
        else:
            l = mid + 1
    return(f"! {l}")

print(bin_search(s))