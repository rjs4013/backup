#여학생 = 0, 남학생 = 1
N, K = map(int, input().split())
S =[]
Y = []
for i in range(N):
    a = list(map(int, input().split()))
    S.append(a[0])
    Y.append(a[1])
Year = [1,2,3,4,5,6]
samesex = []
count = 0
for x in [0, 1]:
    for y in range(N):
        if x == S[y]:
            samesex.append([S[y], Y[y]])

room = [[] for _ in range(12)]

for q in range(N):
    for w in range(6):
        if samesex[q][0] == 0 and samesex[q][1] == Year[w]:
            room[w].append(samesex[q])
        elif samesex[q][0] == 1 and samesex[q][1] == Year[w]:
            room[w+6].append(samesex[q])
for o in room:
    if 0< len(o) <= K: count += 1
    elif len(o) > K:
        if len(o) % K == 0: count += len(o) // K
        else: count += len(o) // K +1

print(count)