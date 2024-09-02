path = [] # 경로를 기록할 리스트
used = [0] * 7


# 0부터 시작, 3개를 뽑은 경우 종료
def recur(level):
    # 1. 기저조건
    if level == 3:
        print(*path)
        return
    # 2. 후보군을 반복하면서
    for i in range(1, 7):
        # i가 이미 뽑혔다면, pass 해라
        # if i in path: continue
        if used[i] == 1: continue

        # 2.1 재귀 호출 전 - 경로 기록 + 사용 기록
        used[i] = 1
        path.append(i)
        # 2.2 다음 재귀 호출(파라미터 전달)
        recur(level+1)
        # 2.3 돌아왔을 때 - 사용했던 경로 삭제
        path.pop()
        used[i] = 0

recur(0)    # 호출: 시작점을 같이 전달해주는 경우가 많다.