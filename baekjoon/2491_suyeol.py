'''
수열 내 연속해서 커지거나(같은 것 포함) or 연속해서 작아지는(같은 것 포함) 수열 중 가장 길이가 긴 것
출력 : 그 길이를 출력
첫 번째 for 문 : i 보다 i+1이 크거나 같다면 cnt+1.... else: cnt 초기화
두 번째 for 문 : i 보다 i+1이 작거나 같다면 cnt+1.... else: cnt 초기화
'''
N = int(input())
arr = list(map(int, input().split()))

# 1로 설정한 이유: 수열 시작할 때 본인 포함해서 시작하기 떄문
cnt = 1     # 계속 업데이트 될 연속된 수열의 수
ans = 1     # 수열 길이의 최댓값
for i in range(N-1):
    if arr[i] <= arr[i+1]:
        cnt += 1
        if ans < cnt:
            ans = cnt
    else:
        cnt = 1

cnt = 1

for i in range(N-1):
    if arr[i] >= arr[i+1]:
        cnt += 1
        if ans < cnt:
            ans = cnt

    else:
        if ans < cnt:
            ans = cnt
        cnt = 1

print(ans)
