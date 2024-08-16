'''
각 기능은 진도가 100% 일 때 서비스에 반영
뒤에 있는 기능은 앞에 있는 기능보다 먼저 개발 가능, 배포 시기는 앞에 있는 기능과 함께 배포
배포는 하루에 한번, 하루의 끝에 이뤄짐

출력 : 각 배포마다 몇 개의 기능이 배포되는가?


'''


def solution(progresses, speeds):
    answer = []
    len_pro = len(progresses)
    stack = []

    for i in range(len_pro):
        day_work = progresses[i]
        count_day = 0
        while day_work < 100:
            day_work += speeds[i]
            count_day += 1

        if not stack:
            stack.append(count_day)

        else:
            if stack[-1] >= count_day:
                stack.append(count_day)

            elif max(stack) < count_day:
                answer.append(len(stack))
                for j in range(len(stack)):
                    stack.pop()
                stack.append(count_day)
            elif max(stack) > count_day > stack[-1]:
                stack.append(count_day)
    answer.append(len(stack))


    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))