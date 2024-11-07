n = int(input())
arr = list(map(int, input().split()))
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    l, r = arr[:mid], arr[mid:]
    left, inv_l = merge_sort(l)
    right, inv_r = merge_sort(r)
    merged, inv_m = merge(left, right)
    return merged, inv_l + inv_r + inv_m

def merge(l, r):
    l_idx, r_idx, inv = 0, 0, 0
    result = []
    while l_idx < len(l) and r_idx < len(r):
        if l[l_idx] <= r[r_idx]:
            result.append(l[l_idx])
            l_idx += 1
        else:
            result.append(r[r_idx])
            r_idx += 1
            inv += len(l) - l_idx
    result += l[l_idx:]
    result += r[r_idx:]
    return result, inv

result, inv = merge_sort(arr)
print(inv)
print(*result)