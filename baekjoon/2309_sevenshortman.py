'''
일곱 난쟁이 키의 합 =  100
출력 -> 일곱 난쟁이 찾아서 오름차순으로 키 출력
'''

tall_list = [int(input()) for _ in range(9)]
a = sum(tall_list)
b = a-100

remo = []
answer = []

for i in range(8):
    if len(remo) == 2:
        break
    for j in range(i+1,9):
        if tall_list[i] + tall_list[j] == b:
            remo.append(tall_list[i])
            remo.append(tall_list[j])
            break

for t in range(9):
    if tall_list[t] not in remo:
        answer.append(tall_list[t])

answer.sort()

for q in answer:
    print(q)