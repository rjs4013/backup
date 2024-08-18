'''
색종이 사이즈는 10x10, 도화지 사이즈는 100x100
방안: 도화지 0으로 2차원 배열만들기 -> 색종이가 붙은 칸에 +1 해주기 -> 도화지에서 0이 아닌 칸 count 하기

'''

N = int(input())
pap_posi = []
entire = [[0] * 100 for _ in range(100)]
for _ in range(N):
    A = list(map(int,input().split()))
    pap_posi.append(A)

for i in pap_posi:
    for j in range(10):
        for q in range(10):
            entire[99-i[1]-j][i[0]+q] = 1


cnt = 0
for a in range(100):
    for b in range(100):
        if entire[a][b] == 0: continue
        cnt += 1

print(cnt)