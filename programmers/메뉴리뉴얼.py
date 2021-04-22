# 1차 시도: 테스트케이스-3/4 정확성: 0, 효율성: 0
from itertools import combinations
from collections import Counter


def solution(orders, courses):

    answer = []
    orders = list(orders)
    for course in courses:
        order_combis = [list(combinations(list(order), course)) for order in orders]
        order_combis = [
            element for order_combi in order_combis for element in order_combi
        ]
        max_order_num = Counter(order_combis).most_common(1)
        if len(max_order_num) == 0 or max_order_num[0][1] == 1:
            continue
        for key, value in Counter(order_combis).items():
            if value == max_order_num[0][1]:
                answer.append("".join(key))
    return sorted(answer)
