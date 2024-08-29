N = 5
arr = [list([0]*7) for _ in range(2)]

for i in range(4):
    arr[0][i] = N+i
    arr[1][-i] = N-i

print(arr)