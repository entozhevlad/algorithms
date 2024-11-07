def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n, k = map(int, input().split())
result = (n * k) // gcd(n, k)
print(result)
