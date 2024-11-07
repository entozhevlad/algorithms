n = 3
nums = [1, 2, 3]
m = [1] * len(nums)
prev_index = [-1] * len(nums)

for i in range(len(nums)-1, -1, -1):
    for j in range(i+1, len(nums)):
        if nums[i] < nums[j] and m[i] < 1 + m[j]:
            m[i] = 1 + m[j]
            prev_index[i] = j

max_length = max(m)
start_index = m.index(max_length)
sequence = []
while start_index != -1:
    sequence.append(nums[start_index])
    start_index = prev_index[start_index]
print(max_length)
print(*sequence)
