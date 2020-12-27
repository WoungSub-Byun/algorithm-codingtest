# 첫번째 풀이 정확도: 91.7%
def solution(n, lost, reserve):
    can_class = n - len(lost)
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            can_class += 1
        elif i - 1 in reserve:
            reserve.remove(i - 1)
            can_class += 1
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            can_class += 1
        if len(reserve) == 0:
            break
    return can_class

