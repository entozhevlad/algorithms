def minecraft_its_my_life(n, h):
    stk = []
    max_area = 0
    idx = 0

    while idx < n:
        if not stk or h[idx] >= h[stk[-1]]:
            stk.append(idx)
            idx += 1
        else:
            top = stk.pop()
            height = h[top]
            width = idx if not stk else idx - stk[-1] - 1
            max_area = max(max_area, height * width)

    while stk:
        top = stk.pop()
        height = h[top]
        width = idx if not stk else idx - stk[-1] - 1
        max_area = max(max_area, height * width)

    return max_area


n = int(input())
h = list(map(int, input().split()))
print(minecraft_its_my_life(n, h))
