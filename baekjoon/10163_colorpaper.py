'''
밑이 행, 옆이 열이라고 생각... 높이, 너비 바꿔서... 정사각형을 시계방향으로 90도 돌린다 생각..
입력 순서대로 각 색종이가 보이는 부분 한 줄에 하나씩 출력
* 색종이가 보이지 않는다면 정수 0 출력
'''

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
# 색종이가 칠해지는 판 만들기 -> 첫번째 색종이는 1로, 두번째 색종이는 2로 ---- -> 겹쳐지는건 계속 숫자가 업데이트 되게 만듬
pan = [[0] * 1001 for _ in range(1001)]

for i in range(N):
    for j in range(paper[i][2]):
        for k in range(paper[i][3]):
            pan[paper[i][0]+j][paper[i][1]+k] = i+1

for q in range(N):
    re_count = 0
    if q == N-1: re_count = paper[q][2] * paper[q][3] # 마지막 색종이는 전체 다 보이니까 넓이 그대로 출력
    else:
        for i in range(paper[q][2]):
            for j in range(paper[q][3]):
                if pan[paper[q][0]+i][paper[q][1]+j] == q+1 : re_count += 1
    print(re_count)
