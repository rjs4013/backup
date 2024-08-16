T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    color_index = [list(map(int, input().split())) for _ in range(N)]
    print(color_index)
    blank_arr = [[0]*10 for _ in range(10)]
    # r1 = [color_index[0][0], color_index[0][1]]
    # c1 = [color_index[1][0], color_index[1][1]]
    # r2 = [color_index[0][2], color_index[0][3]]
    # c2 = [color_index[1][2], color_index[1][3]]
    # color_1 = color_index[0][4]
    # color_2 = color_index[0][4]

    column_dif = color_index[0][3] - color_index[0][1]

    di = [0]*column_dif
    dj = [1]*column_dif

    for x in range(N):
        for i in range(color_index[x][0], color_index[x][2]): # 2~4행
            blank_arr[color_index[x][0]][color_index[x][1]] += 1
            for k in range(len(di)):
                ni = i + di[k]
                nj = i + dj[k]
                blank_arr[color_index[x][ni]][color_index[x][nj]] += 1

        # for k in range(len(di)):
        #     ni = i+di[k]
        #     nj = i