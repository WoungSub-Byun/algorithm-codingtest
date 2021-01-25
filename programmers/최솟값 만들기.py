# 1차 4.4
import numpy as np


def solution(A, B):
    sums_list = []
    for _ in range(len(A)):
        sums_list.append(sum(np.array(A) * np.array(B)))
        tmp = B.pop(0)
        B.append(tmp)
    return int(min(sums_list))
