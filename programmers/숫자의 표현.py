# 1차 100
def solution(n):
    answer = 1
    temp = [0]
    i = 1
    while i < n:
        temp.append(i)
        if sum(temp) == n:
            answer += 1
            i = min(temp)
            temp = []
        if sum(temp) > n:
            i = min(temp)
            temp = []
        i += 1

    return answer