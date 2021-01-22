# 1차 풀이 100
def solution(n):
    answer = n + 1
    while True:
        if bin(n).count("1") == bin(answer).count("1"):
            return answer
        answer += 1


# 2차 풀이 100
def solution(n):
    answer = n + 1
    n = bin(n).count("1")
    while True:
        if n == bin(answer).count("1"):
            return answer
        answer += 1
