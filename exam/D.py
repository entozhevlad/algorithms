MOD = 1000000009

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_three_digit_primes():
    primes = set()
    for num in range(100, 1000):
        if is_prime(num):
            primes.add(num)
    return primes

def count_valid_passwords(N):
    primes = generate_three_digit_primes()
    dp = {prime: 1 for prime in primes}

    for length in range(4, N + 1):
        new_dp = {prime: 0 for prime in primes}
        for prime in dp:
            last_two_digits = prime % 100
            for digit in range(10):
                new_number = last_two_digits * 10 + digit
                if new_number in primes:
                    new_dp[new_number] = (new_dp[new_number] + dp[prime]) % MOD
        dp = new_dp

    result = sum(dp.values()) % MOD
    return result

n = int(input())
print(count_valid_passwords(n))
