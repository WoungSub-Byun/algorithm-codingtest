# 1차 100
def solution(s):
    cnt_open, cnt_close = 0, 0
    for i in s:
        if i == ")":
            cnt_close += 1
        else:
            cnt_open += 1
        if cnt_open < cnt_close:
            return False
    if cnt_open != cnt_close:
        return False
    return True