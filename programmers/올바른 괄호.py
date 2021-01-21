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


# 2차 100
def solution(s):
    x = 0
    for i in s:
        if i == ")":
            x -= 1
        else:
            x += 1
        if x < 0:
            return False
    if x != 0:
        return False
    return True


# 이 문제에서 False가 나오는 경우는 두가지가 있다.
# 1. )가 (의 수보다 많아지는 경우
# 2. ( 와 )의 최종 개수가 다른 경우
# )의 갯수가 (보다 많아지는 경우에는 이후에도 올바르게 바뀌지 않기때문에 for 문에서 검사한다.

# 첫번째 시도에서는 ) 와 (의 갯수를 세는 변수를 따로 지정했었는데 이를 x하나로 해서 (는 +1, )는 -1을 해주어서 변수하나로 검사하였다.