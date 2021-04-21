# 1차 시도: 정확성-100 효율성-0
def solution(info, query):
    info = [i.split() for i in info]
    query = [i.split("and") for i in query]
    for i in range(len(query)):
        for j in range(len(query[i])):
            query[i][j] = query[i][j].strip()
        temp = query[i][-1].split()
        query[i].pop()
        query[i] += temp
    answer = [0] * len(query)
    idx = 0
    for i in query:
        for j in info:
            if (
                (i[0] == "-" or i[0] == j[0])
                and (i[1] == "-" or i[1] == j[1])
                and (i[2] == "-" or i[2] == j[2])
                and (i[3] == "-" or i[3] == j[3])
                and (i[-1] == "-" or int(i[-1]) <= int(j[-1]))
            ):
                answer[idx] += 1
        idx += 1
    return answer


from itertools import combinations as combi
from collections import defaultdict


def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        info = info.split()
        info_key = info[:-1]
        info_val = int(info[-1])
        for i in range(5):
            for c in combi(info_key, i):
                tmp_key = "".join(c)
                info_dict[tmp_key].append(info_val)
    for key in info_dict.keys():
        info_dict[key], sort()
    for query in queries:
        query = query.split(" ")
        query_score = int(query[-1])
        query = query[:-1]

        for i in range(3):
            query.remove("and")
        while "-" in query:
            query.remove("-")
        tmp_q = "".join(query)

        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:
            answer.append(0)
    return answer