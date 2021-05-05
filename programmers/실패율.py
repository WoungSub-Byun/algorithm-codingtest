# 1차 시도: 100%
def solution(N, stages):
    failures = {}

    for n in range(1, N + 1):
        yet_players = len([stage for stage in stages if n <= stage < n + 1])
        reach_players = len([stage for stage in stages if stage >= n])
        if not reach_players:
            failures[n] = 0
        else:
            failures[n] = yet_players / reach_players
    result = sorted(failures.items(), key=lambda x: x[1], reverse=True)

    return [res[0] for res in result]


# 실행시간이 상대적으로 길었는데 sorted 함수를 사용했기 때문인 것 같다.