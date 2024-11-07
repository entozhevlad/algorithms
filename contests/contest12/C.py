import sys

n = int(sys.stdin.readline().strip())

def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, max_num + 1):
        if is_prime[i]:
            for multiple in range(2 * i, max_num + 1, i):
                is_prime[multiple] = False
    return is_prime

is_prime = sieve_of_eratosthenes(n)

for p in range(2, n // 2 + 1):
    if is_prime[p] and is_prime[n - p]:
        sys.stdout.write(f"{p} {n - p}\n")
        break
