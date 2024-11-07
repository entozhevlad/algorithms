p = input()
t = input()
length_t, length_p = len(t), len(p)
num = 0
result = []
for i in range(length_t-length_p+1):
    string = t[i:i+length_p]
    count = 0
    idx = i
    for j in range(length_p):
        if p[j] != string[j]:
            count += 1
        if count > 1:
            break
    if count <= 1:
        num += 1
        result.append(idx+1)
print(num)
print(*result)
#