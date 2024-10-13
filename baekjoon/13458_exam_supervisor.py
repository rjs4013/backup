'''
N개의 시험장, i번 시험장의 응시자수 Ai명
총 감독관(1명) 최대 감시 응시자 수 -> B명
부 감독관(여러명 가능) 최대 감시 응시자 수 -> C명
출력 -> 필요한 감독관 수의 최솟값
'''

N = int(input())
arr = list(map(int,input().split()))
B, C = map(int, input().split())

cnt = 0
for i in arr:
    if i <= B:
        cnt += 1
    else:
        if i-B <= C:
            cnt += 2
        else:
            if (i-B) % C == 0:
                cnt += 1 + (i - B) // C
            else:
                cnt += 2 + (i - B) // C

print(cnt)