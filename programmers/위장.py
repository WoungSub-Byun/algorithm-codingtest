# 첫번째 풀이
from collections import Counter
def solution(clothes):
    items = dict(Counter([i[1] for i in clothes]))

    cnt = 1
    for i in items.values():
        cnt *= (i+1)
    return cnt - 1

# 두번째 풀이
def solution(clothes):
    from collections import Counter
    from functools import reduce
    items = Counter([i[1] for i in clothes])
    return reduce(lambda x, y: x*(y+1), items.values(),1) -1