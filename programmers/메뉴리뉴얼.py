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


from itertools import combinations

# 2번째 시도: set과 & 연산을 사용한 order 중복문자열
def other_solution(orders, course):
    answer = []
    myDict = {}

    for i in range(len(orders)):
        for j in range(i + 1, len(orders)):
            tmp = list(set(orders[i]) & set(orders[j]))  # 두 order에서 겹치는 문자를 리스트로 반환
            tmp.sort()  # 정렬
            tmp = "".join(tmp)  # 리스트 형태를 문자열화

            if len(tmp) > 0:  # 두 order사이 겹치는 문자열이 없을 경우
                for k in course:
                    if k <= len(tmp):  # tmp의 길이가 코스의 길이와 같을때 => 원하는 개수의 메뉴 구성일때
                        comb = list(combinations(tmp, k))  # 겹치는 문자열들 중에서 조합한 경우의 수들
                        for l in range(len(comb)):
                            key = str("".join(comb[l]))  # 모든 경우의 수들을 문자열화하고
                            if key in myDict:  # orders에서 나올 수 있는 모든 조합들의 중복 횟수를 구함
                                myDict[key] += 1
                            else:
                                myDict[key] = 1
    for c in course:
        arr = []
        maxNum = 0
        for key, value in myDict.items():
            if len(key) == c:  # 코스에서 원하는 개수의 조합들 중 가장 많이 나온 조합구하기
                if maxNum < value:  # 문자열이 나온 횟수가 maxNum보다 많을 경우
                    arr = [key]
                    maxNum = value
                elif maxNum == value:  # 조합이 나온 횟수가 maxNum과 같은 경우
                    arr.append(key)
        for i in range(len(arr)):
            answer.append(arr[i])
    answer.sort()

    return answer


print(other_solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
