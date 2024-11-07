def count_digits(num):
    """Count the number of digits in a number."""
    return len(str(num))


def get_answer(i, j, string, dp):
    """Find the optimal compression of a substring."""
    if i == j:
        return string[i]
    if dp[i][j] is not None:
        return dp[i][j]
    res = float('inf')
    for m in range(i, j):
        left = get_answer(i, m, string, dp)
        right = get_answer(m + 1, j, string, dp)
        if len(left) + len(right) < res:
            res = len(left) + len(right)
            dp[i][j] = left + right
    # Check for repeating patterns
    for step in range(1, (j - i + 1) // 2 + 1):
        if (j - i + 1) % step == 0:
            pattern = string[i:i + step]
            if pattern * ((j - i + 1) // step) == string[i:j + 1]:
                compressed = f"{(j - i + 1) // step}({get_answer(i, i + step - 1, string, dp)})"
                if len(compressed) < res:
                    res = len(compressed)
                    dp[i][j] = compressed
    return dp[i][j]


string = input().strip()
n = len(string)
dp = [[None] * n for _ in range(n)]
ans = get_answer(0, n - 1, string, dp)
print(ans)