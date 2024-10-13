'''
S = A[0] * B[0] + ... + A[N-1] * B[N-1] + ...
A -> 재배열 가능
B -> 재배열 불가
최소 S 값을 구하자
B가 재배열 불가니까.. B 큰놈이랑 A 작은놈이랑 곱해야..
그냥 둘다 정렬해서 한 쌍으로 곱한다..
'''

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

sum = 0
for i in range(N):
    sum += A[i] * B[i]

print(sum)