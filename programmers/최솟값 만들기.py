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


# 3차 100
def solution(A, B):
    A = sorted(A)
    B = sorted(B, reverse=True)

    return sum([a * b for a, b in zip(A, B)])


# 1, 2차는 완전탐색
# 3차 때는 A의 가장작은 수와 B의 가장 큰수를 곱했을 때 가장 작은 합계가 나오기 때문에
# A는 내림차순, B는 오름차순으로 정렬하여 합계를 내었다.