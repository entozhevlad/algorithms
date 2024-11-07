t = input()
q = int(input())
length = len(t)
for _ in range(q):
    s = input()
    result = [0]
    n = len(s)
    for i in range(length-n+1):
        if t[i:i+n] == s:
            result[0] += 1
            result.append(i)
    print(*result)
