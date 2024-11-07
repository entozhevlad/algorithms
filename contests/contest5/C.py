import sys
value = 31
mod = int(10 ** 9) + 7

def powers(n):
    pow_list = [1] * (n + 1)
    for i in range(1, n + 1):
        pow_list[i] = (pow_list[i - 1] * value) % mod
    return pow_list

def get_hash(hashes, pow_list, l, r):
    hash_val = (hashes[r] - (hashes[l - 1] * pow_list[r - l + 1] % mod) + mod) % mod
    return hash_val

def hash_function(s):
    hashes = [0] * (len(s) + 1)
    for i in range(len(s)):
        char_value = 0
        if s[i].isalpha():
            char_value = ord(s[i]) - ord('a') + 1 if s[i].islower() else ord(s[i]) - ord('A') + 27
        elif s[i].isdigit():
            char_value = ord(s[i]) - ord('0') + 53
        hashes[i + 1] = (hashes[i] * value + char_value) % mod
    return hashes

def permutation(t, pow_list):
    res = hash_function(t + t)
    hashes = []
    l = 1
    r = len(t)
    for i in range(len(t)):
        hashes.append(get_hash(res, pow_list, l, r))
        l += 1
        r += 1
    return hashes

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

pow_list = powers(2 * len(s))
hashes = hash_function(s)

result = permutation(t, pow_list)

match_count = 0
hash_set = set(result)
for i in range(len(s) - len(t) + 1):
    hash_s = get_hash(hashes, pow_list, i + 1, i + len(t))
    if hash_s in hash_set:
        match_count += 1

sys.stdout.write(f"{match_count}\n")
