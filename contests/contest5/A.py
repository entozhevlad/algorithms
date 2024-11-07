s = input()
m = int(input())
for _ in range(m):
    l1, r1, l2, r2 = map(int, input().split())
    if s[l1-1:r1] == s[l2-1:r2]:
        print("Yes")
    else:
        print("No")

