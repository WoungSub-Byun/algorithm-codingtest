# 첫번째 풀이 : 100


def solution(s):
    new_s = s[2:-2].split("},{")
    serialized_str = []
    for row in new_s:
        serialized_str.append(row.split(","))
    result = []
    for i in range(len(serialized_str)):
        for j in serialized_str:
            if len(j) == i + 1:
                tmp = list(set(j) - set(result))[0]
                result.append(tmp)
    return list(map(int, result))
