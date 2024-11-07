s = list(input())
print(s)
count  = 0
d = {"(": ")", "[": "]", "{": "}" }
for i in range(len(s)):
    if s[i] in "([{":
        count+= 1
    elif s[i] in ")]}" and count > 0:
        count -= 1
        if d[s[count]] != s[i]:
            s[count] = ''
            s[i] = ''
    else:
        s[i] = ''
print(" ".join(s))

