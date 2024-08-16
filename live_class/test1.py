data = [0, 4, 1, 3, 1, 2, 4, 1]
counts = [0] * 5
N = len(data)
TEMP = [0] * N

# counts[0] += 1
# counts[4] += 1
# counts[1] += 1
# counts[3] += 1
# counts[1] += 1
# counts[2] += 1
# counts[4] += 1
# counts[1] += 1

# print(counts)

for i in data:
    counts[i] += 1                          # data의 원소 i를 가져와서 counts[i]에 개수 기록
print(counts)

for i in range(1, len(counts)):             # counts[1] ~ counts[4]까지 누적개수
    counts[i] += counts[i-1]
print(counts)

for i in range(len(TEMP)-1,-1,-1):
    counts[data[i]] -= 1                    # 누적개수 1개 감소
    TEMP[counts[data[i]]] = data[i]
print(TEMP)