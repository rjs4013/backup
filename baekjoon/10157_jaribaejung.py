C, R = map(int,input().split())
K = int(input())

arr = [[0] * C for _ in range(R)]

num = 1
top, bottom = 0, R-1
left, right = 0, C-1

while top <= bottom and left <= right:
    for i in range(bottom, top - 1, -1):
        if num > C*R: continue
        arr[i][left] = num
        num += 1
    left += 1

    for i in range(left, right +1):
        if num > C * R: continue
        arr[top][i] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        if num > C * R: continue
        arr[i][right] = num
        num += 1
    right -= 1

    for i in range(right, left-1, -1):
        if num > C * R: continue
        arr[bottom][i] = num
        num += 1
    bottom -=1

ans = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == K:
            ans = [j+1, R-i]
            break



if ans: print(' '.join(map(str, ans)))
else: print(0)

