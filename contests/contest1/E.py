from math import sqrt
a,b,c,d = map(int, input().split())
def bin_search(a,b,c,d):
    b /= a
    c /= a
    d /= a
    l, r  = -100000000000000, 100000000000000
    while r - l >= 1/10000:
        m = (l + r) / 2
        ur = (m**3) + b*(m**2) + c*m + d
        if ur == 0:
            return m
        elif ur < 0:
            l = m
        else:
            r = m
    return (l + r) / 2

print(bin_search(a,b,c,d))