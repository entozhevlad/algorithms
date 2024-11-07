import sys
MOD = 10**9+7

def mod_exp(x, y, p):
    result = 1
    base = x % p
    exp = y
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        exp //= 2
    return result


n, k = map(int, sys.stdin.readline().strip().split())
factorial = [1] * (n + 1)
for i in range(2, n + 1):
    factorial[i] = factorial[i - 1] * i % MOD
inv_factorial = [1] * (n + 1)
inv_factorial[n] = mod_exp(factorial[n], MOD - 2, MOD)
for i in range(n - 1, -1, -1):
    inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % MOD
result = factorial[n] * inv_factorial[k] % MOD * inv_factorial[n - k] % MOD
sys.stdout.write(f"{result}\n")

