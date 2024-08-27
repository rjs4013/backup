'''
연속적인 k일 동안의 합이 가장 큰 값 출력
시간 초과 주의..
'''

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 첫 번째 범위 내 합 계산
current_sum = sum(arr[:K])
max_sum = current_sum

# 이전 계산 한 합에서 첫 번째 요소를 뺴고, 새로 추가된 요소를 합에 더함.
# 두 개의 연산으로 새로운 값 구할 수 있어짐
for i in range(1, N - K + 1):
    current_sum = current_sum - arr[i - 1] + arr[i + K - 1]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)

# 시간 초과해서 망한 코드... 매번 슬라이싱해서 sum 하니까 시간 복잡도 커짐
# ans = []
# for i in range(N-(K-1)):
#     ans.append(sum(arr[i:i+K]))
#
# print(max(ans))