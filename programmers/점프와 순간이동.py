# 1차시도: 100% 진짜 빠르게 맞췄다.... 2분도 안걸렸던거 같다.
def solution(n):
    answer = 0
    while n:
        if n % 2 != 0:
            n -= 1
            answer += 1
        else:
            n /= 2
    return answer