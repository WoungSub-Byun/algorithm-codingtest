# 첫번째 풀이 정확도 66.7 효율성 0 -> 66.7 / 100
def solution(prices):
    answer = []
    time = 1
    for idx in range(len(prices)):
        if prices[idx] == min(prices[idx:]):
            answer.append(len(prices[idx:]) - 1)
        else:
            for j in prices[idx+1:]:
                if j < prices[idx]:
                    answer.append(time)
                    time = 1
                    break
                else:
                    time += 1
    return answer


# 두번째 풀이
from collections import deque

def solution2(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()
        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1
        answer.append(count)
    return answer
