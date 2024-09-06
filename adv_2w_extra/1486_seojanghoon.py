'''
탑의 높이가 B 이상인 경우 선반 위 물건 이용 가능,
높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑 알아내기
부분집합,,, 현재 직원의 키를 포함하거나? 안하거나?,,, 백트래킹,,,
'''
def height(n, current_sum):
    global top_min
    if current_sum >= B :
        top_min = min(top_min, current_sum)
        return

    if n == N:
        return

    height(n+1, current_sum + arr[n]) # 현재 값 포함
    height(n+1, current_sum) # 현재 값 미포함



T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int,input().split()))

    top_min = float('inf')
    height(0, 0)

    print(f'#{test_case} {top_min-B}')
