n = int(input())
ans = []
i = 2
while i * i <= n:
    count = 0
    while n % i == 0:
        n //= i
        count += 1
    if count == 1:
        ans.append(str(i))
    elif count > 1:
        ans.append(f"{i}^{count}")
    i += 1
if n > 1:
    ans.append(str(n))
print("*".join(ans))


