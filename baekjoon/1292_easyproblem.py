A, B = map(int,input().split())

numbers= []

for i in range(1, 1000):
    numbers.extend([i] * i) # i를 i번 반복에서 numbers에 넣음

ans = sum(numbers[A-1:B]) # 합 구하기
print(ans)
