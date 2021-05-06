# 1차 시도 : 53%
from collections import Counter


def solution(str1, str2):
    # 1. 모두 소문자로 변환
    str1, str2 = str1.lower(), str2.lower()
    # 2. 다중 집합만들기
    multiple_sets = [[], []]
    cnt = 0
    for idx, st in enumerate([str1, str2]):
        for char in st:
            if not cnt:
                cnt += 1
                prev = char
                continue
            if not (char.isalpha() and prev.isalpha()):
                cnt = 0
                continue
            multiple_sets[idx].append(prev + char)
            prev = char
        cnt = 0

    # 3. 원소의 개수 구해서 교집합, 합집합 길이 구하기
    set_count = [dict(Counter(st)) for st in multiple_sets]
    # 4. 교집합 구하기
    min_sets = list(set(set_count[0].keys()) & set(set_count[1].keys()))
    # 5. 합집합 구하기
    max_sets = list(set(set_count[0].keys()) | set(set_count[1].keys()))

    result = [0, 0]
    for char in min_sets:
        min_num = (
            set_count[0][char]
            if set_count[0][char] < set_count[1][char]
            else set_count[1][char]
        )
        result[0] += min_num
    for char in max_sets:
        max_num = 0
        if char in set_count[0]:
            max_num = set_count[0][char]
        if char in set_count[1]:
            max_num = (
                max(max_num, set_count[1][char]) if not max_num else set_count[1][char]
            )
        result[1] += max_num
    if not result[1]:
        return 65536
    return int((result[0] / result[1]) * 65536)


# 2차 시도: 61.5
from collections import Counter


def solution(str1, str2):
    # 1. 모두 소문자로 변환
    str1, str2 = str1.lower(), str2.lower()
    # 2. 다중 집합만들기
    multiple_sets = [[], []]
    cnt = 0
    multiple_sets[0] = [
        (str1[i] + str1[i + 1])
        for i in range(len(str1) - 1)
        if (str1[i] + str1[i + 1]).isalpha()
    ]
    multiple_sets[1] = [
        (str2[i] + str2[i + 1])
        for i in range(len(str2) - 1)
        if (str2[i] + str2[i + 1]).isalpha()
    ]

    # 3. 원소의 개수 구해서 교집합, 합집합 길이 구하기
    set_count = [dict(Counter(st)) for st in multiple_sets]
    # 4. 교집합 구하기
    min_sets = list(set(set_count[0].keys()) & set(set_count[1].keys()))
    # 5. 합집합 구하기
    max_sets = list(set(set_count[0].keys()) | set(set_count[1].keys()))

    result = [0, 0]
    for char in min_sets:
        min_num = (
            set_count[0][char]
            if set_count[0][char] < set_count[1][char]
            else set_count[1][char]
        )
        result[0] += min_num
    for char in max_sets:
        max_num = 0
        if char in set_count[0]:
            max_num = set_count[0][char]
        if char in set_count[1]:
            max_num = (
                max(max_num, set_count[1][char]) if not max_num else set_count[1][char]
            )
        result[1] += max_num
    if not result[1]:
        return 65536
    return int((result[0] / result[1]) * 65536)

    from collections import Counter
