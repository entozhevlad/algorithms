m_c = (1 * 2 ** 31)
n = int(input())
a = [0] + list(map(int, input().split())) + [0]
d = [float("inf")] + list(map(int, input().split())) + [float("inf")]
m = [[i-1, i + 1] for i in range(n+2)]
m_d = []
res = []
next_r = set()
my_r = [i for i in range(1, n+1)]
b = [0] + [1 for i in range(n)] + [0]

for x in range(n):
    m_d = []
    for i in my_r:
        if m[i] != -1 and (d[i] - a[m[i][0]] - a[m[i][1]] < 0):
            m_d.append(i)
            b[i] = 0
    res.append(len(m_d))
    next_r = set()
    for i in m_d:
        m[m[i][0]][1] = m[i][1]
        m[m[i][1]][0] = m[i][0]
        if b[m[i][0]]:
            next_r.add(m[i][0])
        if b[m[i][1]]:
            next_r.add(m[i][1])
        m[i] = -1
    my_r = next_r

print(*res)
