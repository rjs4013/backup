S = list(map(str,input()))
blank_list = [0] * 26

for i in range(len(blank_list)):
    blank_list[i] = chr(97+i)

for k, v in enumerate(S):
    for j in range(len(blank_list)):
        if v == blank_list[j]:
            blank_list[j] = k
            break

for a in range(len(blank_list)):
    if not type(blank_list[a]) == int:
        blank_list[a] = -1
ans = ' '.join(map(str, blank_list))
print(ans)