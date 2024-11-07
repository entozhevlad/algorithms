import sys
def calculate(numbers):
    st = []
    prefix_sum = [0] * (len(numbers) + 1)
    result = 0

    for i in range(len(numbers)):
        prefix_sum[i + 1] = prefix_sum[i] + numbers[i]

    i = 0
    while i <= len(numbers):
        while st and (i == len(numbers) or numbers[st[-1]] > numbers[i]):
            last_element = st.pop()
            result = max(result, (prefix_sum[i] - prefix_sum[0 if not st else st[-1] + 1]) * numbers[last_element])
        st.append(i)
        i += 1

    return result

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
result = calculate(numbers)
sys.stdout.write(f"{result}\n")


