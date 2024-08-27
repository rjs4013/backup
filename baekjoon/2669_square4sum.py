'''
x, y 축바꿔서 matrix에 색종이 칠할 부분 1로 기록
1 count 해서 면적구하기
'''

matrix = [list([0] * 100) for _ in range(100)]
arr = [list(map(int, input().split())) for _ in range(4)]

for i in range(4):                                      # 직사각형 4개
    for j in range(arr[i][2]-arr[i][0]):                # 밑변
        for k in range(arr[i][3] - arr[i][1]):          # 높이
            matrix[arr[i][1] + k][arr[i][0] + j] = 1    # 밑변, 높이 증가하면서 색칠하기

cnt = 0

for a in range(len(matrix)):
    for b in range(len(matrix)):
        if matrix[a][b] != 1:
            continue
        cnt += 1

print(cnt)