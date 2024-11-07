n = int(input())
def AntiQSort(n):
    if n == 1:
        return [1]
    arr = [1, 2]
    for i in range(3, n + 1):
        arr.append(i)
        arr[(len(arr)-1)//2], arr[i-1] = arr[i-1], arr[(len(arr)-1)// 2]
    return arr

print(*AntiQSort(n))