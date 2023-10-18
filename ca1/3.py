txt = input()
max_len = 0
cur = 0

for i in range(1, len(txt) + 1):
    max_len = max(max_len, i - cur)
    if i > len(txt) - 1:
        break
    char_pos = txt[cur:i].find(txt[i])
    if char_pos != -1:
        cur += char_pos + 1

print(max_len)
