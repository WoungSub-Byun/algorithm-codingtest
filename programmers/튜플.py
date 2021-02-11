# 첫번째 풀이 : 100


def solution(s):
    new_s = s[2:-2].split("},{")  # 맨앞과 맨뒤 없애고 원소만 남게 split
    serialized_str = []
    for row in new_s:
        serialized_str.append(row.split(","))  # 제대로된 리스트 serialized_str
    result = []
    for i in range(len(serialized_str)):  # 결과 튜플의 길이만큼
        for j in serialized_str:
            if len(j) == i + 1:  # 순서대로 정렬하는 대신 길이가 1부터 튜플의 길이까지
                tmp = list(set(j) - set(result))[
                    0
                ]  # 현재 원소에서 result에 이미 들어가있는 원소 빼기 : 차집합 구하기
                # 결과가 리스트이기 때문에 0번째 인덱스의 원소를 append
                result.append(tmp)
    return list(map(int, result))  # str형태의 원소들을 int로 매핑해주고 returns


# 두번째 풀이


def solution(s):
    new_s = s[2:-2].split("},{")  # 맨앞과 맨뒤 없애고 원소만 남게 split
    serialized_str = []
    for row in new_s:
        serialized_str.append(row.split(","))  # 제대로된 리스트 serialized_str
    serialized_str.sort(key=len)  # 원소들의 길이를기준으로 정렬
    result = []
    for row in serialized_str:  # 결과 튜플의 길이만큼
        tmp = list(set(row) - set(result))[
            0
        ]  # 현재 원소에서 result에 이미 들어가있는 원소 빼기 : 차집합 구하기
        # 결과가 리스트이기 때문에 0번째 인덱스의 원소를 append
        result.append(tmp)
    return list(map(int, result))  # str형태의 원소들을 int로 매핑해주고 returns
