MAX = 100005

arr = [0] * MAX
tree = [[0] * (4 * MAX) for _ in range(21)]
lazy = [[0] * (4 * MAX) for _ in range(21)]

def build(no, n):
    for i in range(n):
        tree[no][n + i] = 1 if arr[i] & (1 << no) else 0
    for i in range(n - 1, 0, -1):
        tree[no][i] = tree[no][i * 2] + tree[no][i * 2 + 1]

def apply(no, p, length):
    tree[no][p] = length - tree[no][p]
    if p < MAX:
        lazy[no][p] ^= 1

def build_lazy(no, p, length):
    for s in range(MAX.bit_length(), 0, -1):
        k = p >> s
        if lazy[no][k]:
            apply(no, k * 2, length >> 1)
            apply(no, k * 2 + 1, length >> 1)
            lazy[no][k] = 0

def update(no, n, l, r):
    l += n
    r += n + 1
    l0, r0 = l, r
    length = 1
    while l < r:
        if l & 1:
            apply(no, l, length)
            l += 1
        if r & 1:
            r -= 1
            apply(no, r, length)
        l //= 2
        r //= 2
        length *= 2
    l, r = l0, r0
    length = 1
    while l > 1:
        l //= 2
        length *= 2
        tree[no][l] = tree[no][l * 2] + tree[no][l * 2 + 1]
        if lazy[no][l]:
            tree[no][l] = length - tree[no][l]
    length = 1
    while r > 1:
        r //= 2
        length *= 2
        tree[no][r] = tree[no][r * 2] + tree[no][r * 2 + 1]
        if lazy[no][r]:
            tree[no][r] = length - tree[no][r]

def query(no, n, l, r):
    l += n
    r += n + 1
    res = 0
    length = 1
    build_lazy(no, l, length)
    build_lazy(no, r - 1, length)
    while l < r:
        if l & 1:
            res += tree[no][l]
            l += 1
        if r & 1:
            r -= 1
            res += tree[no][r]
        l //= 2
        r //= 2
        length *= 2
    return res

def main():
    n = int(input().strip())
    arr_input = input().strip().split()
    for i in range(n):
        arr[i] = int(arr_input[i])

    for i in range(20):
        build(i, n)

    m = int(input().strip())
    result = []
    for _ in range(m):
        command = list(map(int, input().strip().split()))
        if command[0] == 1:
            l, r = command[1], command[2]
            total_sum = 0
            for i in range(20):
                total_sum += query(i, n, l - 1, r - 1) * (1 << i)
            result.append(total_sum)
        else:
            l, r, x = command[1], command[2], command[3]
            for i in range(20):
                if x & (1 << i):
                    update(i, n, l - 1, r - 1)

    for res in result:
        print(res)

if __name__ == "__main__":
    main()
