T = int(input())
for t in range(1,T+1):
    a = input()
    b = list(a)
    c = len(b)
    for i in range(c//2):
        b[i], b[c-i-1] = b[c-i-1], b[i]
    for x in range(c):
        if b[x] == 'b':
            b[x] = 'd'
        elif b[x] == 'd':
            b[x] = 'b'
        elif b[x] == 'p':
            b[x] = 'q'
        elif b[x] == 'q':
            b[x] = 'p'
    print(f'#{t} {"".join(b)}')