# 1차 4.4
import numpy as np


def solution(A, B):
    sums_list = []
    for _ in range(len(A)):
        sums_list.append(sum(np.array(A) * np.array(B)))
        tmp = B.pop(0)
        B.append(tmp)
    return int(min(sums_list))


# 2차 4.4
def solution2(A, B):
    sums_list = []
    for _ in range(len(A)):
        sums_list.append(sum([A[i] * B[i] for i in range(len(B))]))
        tmp = B.pop(0)
        B.append(tmp)
    return min(sums_list)
