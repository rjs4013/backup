T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    mountain_list = []
    count_j = 0
    j = 0
    a = 0
    while count_j < N:
        for x in range(0,1):
            for y in range(1,N):
                if arr[x] < arr[y]:
                    a += 1
        if a == 0:
            break
        if j + 1 >= N-1:
            break
        j = count_j
        while arr[j] <= arr[j+1]:
            j += 1
            if j + 1 >= N-1:
                mountain_list.append(arr[count_j:N])
                break
        else:
            mountain_list.append(arr[count_j:j+1])
            count_j = j+1

    count1 = float('inf')
    answer = 0
    for i in range(len(mountain_list)):
        max1 = float('inf')
        min1 = float('-inf')
        for j in range(len(mountain_list[i])):
            if max1 < mountain_list[i][j]:
                max1 = mountain_list[i][j]
            if min1 > mountain_list[i][j]:
                min1 = mountain_list[i][j]
        count2 = (max1 - min1)/len(mountain_list[i])
        if count2 < count1:
            count1 = count2
            answer = len(mountain_list[i])
        if count2 == count1 and len(mountain_list[i]) > answer:
            answer = len(mountain_list[i])
    if a != 0:
        print(f'#{test_case} {answer}')
    else:
        print(f'#{test_case} 0')

