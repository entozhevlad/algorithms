MAX_LEN = 10**9

def count(num):
    amount = 0
    while num:
        num //= 10
        amount += 1
    return amount

def get_answer(i, j, string):  # Renaming the variable to avoid conflict
    if i == j:
        return string[i]
    res = MAX_LEN
    LEN = j - i + 1
    for step in range(1, LEN // 2 + 1):
        if LEN % step != 0:
            continue
        is_ok = True
        for cur in range(step):
            for pos in range(i + cur, j + 1, step):
                if string[i + cur] != string[pos]:
                    is_ok = False
                    break
        if is_ok:
            cur_len = count((j - i + 1) // step) + 2 + mas[i][i + step - 1]
            if cur_len == mas[i][j]:
                return str((j - i + 1) // step) + "(" + get_answer(i, i + step - 1, string) + ")"
    for m in range(i, j):
        if mas[i][m] + mas[m + 1][j] == mas[i][j]:
            return get_answer(i, m, string) + get_answer(m + 1, j, string)


string = input("Введите строку: ").strip()
n = len(string)  # Renaming the variable to avoid conflict
mas = [[0] * n for _ in range(n)]
for length in range(n):
    for i in range(n):
        j = i + length
        if j >= n:
            break
        if length == 0:
            mas[i][j] = 1
        else:
            res = MAX_LEN
            LEN = j - i + 1
            for step in range(1, LEN // 2 + 1):
                if LEN % step != 0:
                    continue
                is_ok = True
                for cur in range(step):
                    for pos in range(i + cur, j + 1, step):
                        if string[i + cur] != string[pos]:
                            is_ok = False
                            break
                if is_ok:
                    cur_len = count(LEN // step) + 2 + mas[i][i + step - 1]
                    res = min(res, cur_len)
            for m in range(i, j):
                res = min(res, mas[i][m] + mas[m + 1][j])
            mas[i][j] = res
ans = get_answer(0, n - 1, string)  # Passing the string as an argument
print(ans)



