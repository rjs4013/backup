'''
설탕을 최대한 적은 봉지에 담아 배달해야함.
봉지의 종류 -> 3kg or 5kg
정확하게 N kg을 만들 수 없다면 -1 출력
'''

N = int(input())

ans = 0
while N >= 0:
    if N % 5 == 0: # 5의 배수?
        ans += N // 5
        print(ans)
        break
    N -= 3 # 3kg 봉지 하나씩 생성
    ans += 1
else:   # 출력이 안되고 끝났다..-> 음수가 되었다 -> 나눠 떨어지지 못했다
    print(-1)