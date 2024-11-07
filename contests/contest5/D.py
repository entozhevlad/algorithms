s = input()
result = s
for i in range(1, len(s)):
    tmp = s[i:] + s[:i]
    if tmp < result:
        result = tmp
print(result)





