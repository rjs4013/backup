'''
3장의 카드를 고르는데, 그 합이 M이 넘지않으면서 M과 최대한 가깝게
'''

N, M = map(int,input().split())
cards = list(map(int, input().split()))

n_list = []

for i in range(N-2):
    for j in range(i+1, N):
        for q in range(j+1, N):
            n_list.append([cards[i],cards[j],cards[q]])

pre_answer = 0

for w in n_list:
    if sum(w) <= M:
        if pre_answer < sum(w):
            pre_answer = sum(w)
print(pre_answer)
