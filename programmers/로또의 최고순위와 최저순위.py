# 1차 시도: 100%
def solution(lottos, win_nums):
    min_num = len(list(set(lottos)) + win_nums) - len(set(list(set(lottos)) + win_nums))
    max_num = min_num + lottos.count(0)
    if max_num < 2:
        return [6, 6]
    min_rank = 6 if min_num < 2 else 7 - min_num
    max_rank = 7 - max_num
    return [max_rank, min_rank]


# 다른 사람들 풀이 중 참신한 방법
def other_solution(lottos, win_nums):

    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans], rank[ans]
