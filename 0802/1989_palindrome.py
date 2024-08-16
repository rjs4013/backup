# 1
T = int(input())

for t in range(1, T+1):
    text_1 = str(input())
    a1 = list(text_1)
    b = len(a1)
    for i in range(b//2):
        a1[i], a1[b-i-1] = a1[b-i-1], a1[i]
    if text_1 == ''.join(a1):
        print(f'#{t} {1}')
    else:
        print(f'#{t} {0}')

# 2
T = int(input())

for tc in range(1, T+1):
    s = input()
    N = len(s)
    ans = 1
    for i in range(N//2):
        if s[i] != s[N-1-i]:
            ans = 0
            break
    print(f'#{tc} {ans}')



