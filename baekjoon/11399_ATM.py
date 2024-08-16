'''
Pi -> i번째 사람이 돈을 인출하는데 걸리는 시간
오름차순정렬 -> 자릿수 슬라이싱해서 더하면 끝
'''



N = int(input())
Pi = list(map(int, input().split()))

for i in range(len(Pi)-1):
    for j in range(i+1, len(Pi)):
        if Pi[i] > Pi[j]:
            Pi[i], Pi[j] = Pi[j], Pi[i]

pre_answer = []
for i in range(N):
    pre_answer.append(sum(Pi[:i+1]))

answer = sum(pre_answer)

print(answer)