# 1 (stack 1)
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    pascal_tri = [[] for _ in range(N)]
    pascal_tri[0].append(1)
    for i in range(1, N):
        stack = pascal_tri[i-1][:]
        pascal_tri[i].append(1)
        for j in range(1, i):
            pascal_tri[i].append(stack.pop() + stack[-1])
        pascal_tri[i].append(1)

    for x in pascal_tri:
        print(*x)

# ---------------------------------------------------------------------

# 2 (재귀)
# row, col 이 주어졌을 때, 이전 row와 col을 구해가면서 현재 row, col을 구하는 재귀함수
def pascal_triangle(row, col):
    # 첫 번째 열이거나 마지막 열인 경우
    # 기저 조건, 재귀가 끝나는 지점
    if col == 0 or col == row:
        return 1

    # 재귀적으로 위 두 값을 더함
    return pascal_triangle(row - 1, col - 1) + pascal_triangle(row - 1, col)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')

    for i in range(N):
        row = []
        for j in range(i + 1):
            row.append(str(pascal_triangle(i, j)))
        print(' '.join(row))

# 재귀 함수를 짤 때는 재귀가 끝나는 지점과 기저 조건을 항상 생각해야한다.
# 그림 그려놓고 짜보기 # 코드는 간단해보이지만 사고 과정이 쉽지 않음.

# ------------------------------------------------------------------------

# 3 (재귀 2)

"""
개선된 재귀를 활용해서 구현
시간복잡도: O(N^2), 조금 빠름
"""
def pascal_triangle(n):
    # 첫 번째 행은 항상 [1]
    if n == 1:
        return [1]

    # 재귀적으로 파고들어서 첫 번째 행부터 값을 구해서 위로 올라감
    prev_row = pascal_triangle(n-1)

    # 새로운 행의 시작은 항상 1
    new_row = [1]

    # 이전 행의 2개의 값을 더해서 새로운 행에 추가함
    # 여기서 이전 행은 재귀적으로 구해나간다.
    for i in range(len(prev_row) - 1):
        new_row.append(prev_row[i] + prev_row[i+1])

    # 새로운 행의 마지막은 항상 1
    new_row.append(1)

    return new_row


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')

    # 각 행에 대해서 출력
    for i in range(1, N+1):
        row = pascal_triangle(i)
        print(' '.join(map(str, row)))

# -----------------------------------------------------------------

# 4 stack2

"""
스택을 활용해서 구현
시간복잡도 O(N^2), 조금 빠름 (개선된 재귀보다 오버플로우 걱정이 덜해서 유리)
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')

    # 첫 번째 행은 항상 [1]
    prev_stack = [1]
    print(1)

    # 파스칼 삼각형은 1로 시작해서 1로 끝나고, 그 사이값은 이전 행의 두 값의 합으로 구성된다.
    # 첫 번째 줄은 이미 [1]로 세팅을 했기 때문에, 2번째 줄부터 진행
    for i in range(1, N):
        new_stack = [1]  # 새로운 행은 항상 1로 시작

        # 이전 행의 인접한 두 수를 더하여 새로운 행 생성
        # 2개씩 더하기 때문에, 윗 줄의 총 개수 - 1개 만큼 더해야 한다. ( 안그러면 터짐 )
        for j in range(len(prev_stack) - 1):
            new_stack.append(prev_stack[j] + prev_stack[j + 1])

        new_stack.append(1)  # 행의 마지막은 항상 1

        # 방금 생성한 파스칼 출력
        print(' '.join(map(str, new_stack)))

        prev_stack = new_stack  # 다음 반복을 위해 스택 업데이트
# -----------------------------------------------------------------

# 5 memorization

"""
memoization을 활용해서 구현 
시간 복잡도: O(N^2) - 좀 더 빠름 

개선된 재귀와 동일하게 코드를 작성하나
기존 행을 계산한 적 있으면 해당 값을 사용하며, 사용한 적이 없으면 값을 계산한 다음에 memo에 저장한다.
"""
def pascal_triangle(n, memo={}):
    if n == 1:
        return [1]

    if n in memo:
        return memo[n]

    prev_row = pascal_triangle(n - 1, memo)
    new_row = [1]

    for i in range(len(prev_row) - 1):
        new_row.append(prev_row[i] + prev_row[i + 1])

    new_row.append(1)
    memo[n] = new_row
    return new_row


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')

    memo = {}
    for i in range(1, N + 1):
        row = pascal_triangle(i, memo)
        print(' '.join(map(str, row)))

# -----------------------------------------------------------------

# 6 DP

"""
DP를 활용해서 구현 
시간 복잡도: O(N^2) - 좀 더 더 빠름 

memoization과 달리 가장 윗 줄부터 계산하면서 깊게 들어간다.
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')

    # 파스칼 삼각형을 저장할 2차원 배열을 생성
    triangle = [[0] * N for _ in range(N)]

    # 모든 행의 첫 번째 열과 마지막 열을 1로 초기화
    for i in range(N):
        triangle[i][0] = 1
        triangle[i][i] = 1

    # 파스칼 삼각형의 값을 아래값부터 게산하면서 올라감
    # for i in range(2, N):
    for i in range(N):
        for j in range(1, i):
            # 이전 행의 2개의 값을 합쳐서, 현재 행에 저장
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    for i in range(N):
        # 각 행에서 i행이면 i번째까지만 출력
        # 왜냐면 나머지는 0으로 채웠기 때문
        print(' '.join(map(str, triangle[i][:i + 1])))

