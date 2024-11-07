def ins_sort(arr):
    for i in range(1,len(arr)):
        curr = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < curr:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = curr
a = [3,1,2,5,4]
ins_sort(a)
print(a)