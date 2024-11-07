n = int(input())
s = input()
alphabet = [0] * 26
for char in s:
    idx = ord(char) - ord('A')
    alphabet[idx] += 1
first = ""
for i in range(26):
    first += chr(ord('A') + i) * (alphabet[i] // 2)
mid = ""
for i in range(26):
    if alphabet[i] % 2 != 0:
        mid = chr(ord('A') + i)
        break
result = first + mid + first[::-1]
print(result)
