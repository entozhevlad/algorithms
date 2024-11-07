from datetime import time

def checker(zeit, hour, minute, second):
    open, close, cur = time(*zeit[:3]), time(*zeit[3:]), time(hour, minute, second)
    if open < close:
        return open <= cur < close
    return cur >= open or cur < close

n = int(input())
arr = []
for _ in range(n):
    zeit = list(map(int, input().split()))
    arr.append(zeit)
result = sum(
        all(checker(zeit, hour, minute, second) for zeit in arr)
        for hour in range(24)
        for minute in range(60)
        for second in range(60)
    )
print(result)
