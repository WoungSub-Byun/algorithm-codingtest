# 첫번째 풀이 - 정확도 10 + 효율성 0 = 10점
def solution(n):
    answer = ''
    steps = ['4', '1', '2']
    while n > 3:
        answer += steps[n % 3]
        n //= 3
    answer += steps[n % 3]
    return answer[::-1]


# 두번째 풀이
def solution(n):
    if n <= 3:
        return '124'[n - 1]
    else:
        q, r = divmod(n - 1, 3)
        return solution(q) + '124'[r]
