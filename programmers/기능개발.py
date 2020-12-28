# 첫번째 풀이
import math
def solution(progresses, speeds):
    answer = []
    rest_progress = [math.ceil((100 - progresses[i]) / speeds[i])  for i in range(len(progresses)) ]
    stack = 1
    max_num = rest_progress[0]
    i = 1
    while True:
        if i >= len(progresses):
            answer.append(stack)
            break
        if max_num >= rest_progress[i]:
            stack += 1
        else:
            answer.append(stack)
            max_num = rest_progress[i]
            stack = 1
        i+=1
    return answer


# 두번째 풀이
def solution(progresses, speeds):
    Q = []
    for q, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((q - 100) // s):
            Q.append([-((q - 100) // s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]