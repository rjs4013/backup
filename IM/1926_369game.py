N = int(input())
numbers = []
for i in range(1, N+1):
    numbers.append(i)
for x in range(len(numbers)):
    clap = list(map(int, str(numbers[x])))+[0]
    if clap[0] in [3, 6, 9] and clap[1] in [3, 6, 9]:
        numbers[x] = '--'
    elif clap[0] in [3, 6, 9] and clap[1] not in [3, 6, 9]:
        numbers[x] = '-'
    elif clap[0] not in [3, 6, 9] and clap[1] in [3, 6, 9]:
        numbers[x] = '-'

answer = ' '.join(map(str, numbers))
print(answer)
