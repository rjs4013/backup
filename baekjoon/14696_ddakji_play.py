'''
별 - 동그라미 - 네모 - 세모 순으로 전에 그림의 수가 동일하다면 현재 그림의 수가 많은 쪽이 이김 + 4개 다 똑같은 개수라면 무승부
4       3       2     1
'''
N = int(input())
for _ in range(N):
    a_child = list(map(int,input().split()))
    b_child = list(map(int, input().split()))
    drawing = [4, 3, 2, 1]
    for k in drawing:
        a_cnt = 0
        for i in range(1, a_child[0]+1):
            if a_child[i] != k: continue
            a_cnt += 1
        b_cnt = 0
        for i in range(1, b_child[0]+1):
            if b_child[i] != k: continue
            b_cnt += 1
        if a_cnt == b_cnt: continue
        elif a_cnt > b_cnt:
            print('A')
            break
        elif b_cnt > a_cnt:
            print('B')
            break
    else:
        print('D')

