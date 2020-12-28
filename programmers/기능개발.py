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
