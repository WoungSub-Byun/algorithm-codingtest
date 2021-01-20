# 1차 100
import itertools


def solution(numbers, target):
    answer = 0
    sum_numbers = sum(numbers)
    print(sum_numbers)
    num_cases = []
    for i in range(1, len(numbers) + 1):
        case = list(itertools.combinations(numbers, i))
        for i in case:
            tmp = sum_numbers - 2 * sum(i)
            if tmp == target:
                answer += 1
    return answer
