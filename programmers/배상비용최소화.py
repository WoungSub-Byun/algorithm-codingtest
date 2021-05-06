# 1차 시도: 69%
def solution(no, works):

    if no > sum(works):
        return 0
    for n in range(no):
        if no - n > sum(works):
            return 0
        max_idx = works.index(max(works))
        works[max_idx] -= 1
    return sum([work ** 2 for work in works])


# 2차 시도 100%
def solution(no, works):

    if no > sum(works):
        return 0
    for n in range(no):
        works = sorted(works, reverse=True)
        works[0] -= 1
    return sum([work ** 2 for work in works])