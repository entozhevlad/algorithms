import sys
def mod_exp(base, exp, mod):
    result = 1
    b = base % mod
    e = exp
    while e > 0:
        if e % 2 == 1:
            result = result * b % mod
        b = b * b % mod
        e //= 2
    return result

def mod_inverse(a, mod):
    return mod_exp(a, mod - 2, mod)

n, m, k, mod = map(int, sys.stdin.readline().strip().split())
total_passwords = mod_exp(m, n, mod)
k_inverse = mod_inverse(k, mod)
result = total_passwords * k_inverse % mod
sys.stdout.write(f"{result}\n")


