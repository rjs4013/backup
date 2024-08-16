T = int(input())
for t in range(1, T + 1):
    A = input()
    B = list(input())

    i = 0
    while i < len(B) - len(A) + 1:
        if A == ''.join(B[i:i + len(A)]):
            print(f'#{t} {1}')
            break
        else:
            i += 1
    if i > len(B) - len(A):
        print(f'#{t} {0}')

