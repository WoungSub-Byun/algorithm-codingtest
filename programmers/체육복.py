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

# 두번째 풀이
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for r in _reserve:
        if r - 1 in _lost:
            _lost.remove(r - 1)
        elif r + 1 in _lost:
            _lost.remove(r + 1)

    return n - len(_lost)
