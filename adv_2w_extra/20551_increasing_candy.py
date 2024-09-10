'''
1. 세 개의 상자, 상자 내 사탕 개수가 순증가하기를 원함
2. 모든 상자에 1개 이상의 사탕
3. 상자 속 사탕을 삭제함으로써 조건 만족 시키기
출력 -> 1) 조건을 만족할 수 있는가?(안되면 -1)    2) 만족 가능이라면 최소 몇 개의 사탕을 먹어야 하는가?
'''
'''
흠.. 일단 마지막 상자에 있는 사탕의 개수가 1개, 2개 이면 조건x
현재 상자와 다음 상자를 비교 -> 현재 상자가 더 많다면? -> 한개 차이까지 cnt += 1
거꾸로 비교 -> 현재 상자가 더 작거나 같다면? 다음 상자를 -1
'''
T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    l = len(arr)
    cnt = 0
    for i in range(l-1, 0, -1):
        if arr[i] < arr[i-1]:
            cnt += arr[i-1] - arr[i] + 1
            arr[i-1] = arr[i] - 1
            if arr[i-1] <= 0:
                cnt = -1
                break
        elif arr[i] == arr[i-1]:
            cnt += 1
            arr[i-1] -= 1
            if arr[i-1] <= 0:
                cnt = -1
                break
    print(f'#{test_case} {cnt}')
