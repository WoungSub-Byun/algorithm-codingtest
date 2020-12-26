from collections import Counter
def solution(clothes):
    items = dict(Counter([i[1] for i in clothes]))

    cnt = 1
    for i in items.values():
        cnt *= (i+1)
    return cnt - 1