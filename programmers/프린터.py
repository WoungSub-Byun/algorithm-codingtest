# 첫번째 풀이 -> X
from collections import deque
import numpy as np
def solution(priorities, location):
    new_priorities = deque()
    stack = []
    for idx, row in enumerate(priorities):
        new_priorities.append([idx, row])

    for _ in range(len(priorities)):
        if new_priorities == sorted(priorities):
            break
        if new_priorities[0][1] == max(priorities):
            stack.append(new_priorities.popleft())
            continue
        else:
            new_priorities.append(new_priorities.popleft())
    return list(np.array(stack).T[0]).index(location) + 1

#두번째 풀이 -> O
def solution(priorities, location):
    answer = 0
    while priorities != []:
        max_p = max(priorities)
        pop_num = priorities.pop(0)
        if max_p == pop_num:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
        else:
            priorities.append(pop_num)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer