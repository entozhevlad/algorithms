n, c = map(int, input().split())
challenges = []
for i in range(n):
    s, t = map(int, input().split())
    challenges.append((s, s + t, i + 1))
challenges.sort(key=lambda x: x[1])
completed, time = [], 1
for challenge in challenges:
    if challenge[0] >= time:
        completed.append(challenge[2])
        time = challenge[1]
ans = len(completed)
print(ans * c)
print(ans)
print(*completed)
