'''
최소힙 문제에서는 굳이 트리를 그릴 이유가 없다.
일단 트리에 순서대로 저장될 값 입력하기
=> 이때 입력된 값과 부모노드 비교해서 바꿔주기(최소 or 최대 힙에 따라)
근데 이때 부모노드를 어떻게 비교하냐? 현재 자신의 인덱스에서 //2 한 값이 결국 부모노드의 인덱스임
바꿔준 후엔 비교될 값을 방금 검색한 그 인덱스로 업뎃 -> while 문 (루트 노드일때까지)
'''
def enqueue(node):
    while node//2:
        parent = node // 2
        if tree[node] <= tree[parent]:
            tree[parent], tree[node] = tree[node], tree[parent]
        node = parent

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    tree = [0]
    last_node = 0
    for i in arr:
        tree.append(i)
        last_node += 1
        enqueue(last_node)

    result = 0

    while last_node:
        parent = last_node//2
        result += tree[parent]
        last_node = parent
    print(f'#{test_case} {result}')