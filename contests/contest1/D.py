from math import sqrt
c = float(input())
def bin_search(c):
    l, r = 0, c
    while r - l >= 1/1000000:
        m = (l + r) / 2
        ur = m**2 + sqrt(m + 1)
        if ur < c:
            l = m
        else:
            r = m
    return (l + r) / 2

print(bin_search(c))
