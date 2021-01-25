# 1차 100
def solution(s: str):
    s_list = sorted(list(map(int, s.split())))
    return "{} {}".format(s_list[0], s_list[-1])