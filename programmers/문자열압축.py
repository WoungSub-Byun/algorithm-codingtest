# 1차 96
def solution(s):

    result = []
    prev_i = 0
    for i in range(len(s) // 2, 0, -1):
        if prev_i == i:
            continue
        prev_i = i
        res = ""
        first_idx = 0
        second_idx = i
        cnt = 1

        while second_idx < len(s) + i:
            tmp = s[first_idx:second_idx]
            tmp_2 = s[second_idx : second_idx + i]
            if tmp == tmp_2:
                cnt += 1
            else:
                res += (str(cnt) + tmp) if cnt != 1 else tmp
                cnt = 1
            first_idx = second_idx
            second_idx += i

        result.append(len(res))

    return min(result)


# 풀이 방법
# for i in range(len(s) // 2, 0, -1):
# 여기서 자를 범위를 큰 숫자부터 돌린다.
# len(s) // 2를 한 이유는 가장 긴 범위가 문자열의 절반 접는 경우이기 때문이다.


# 2차 100
def solution(s):
    if len(s) == 1:
        return 1
    result = []
    prev_i = 0
    for i in range(len(s) // 2, 0, -1):
        if prev_i == i:
            continue
        prev_i = i
        res = ""
        first_idx = 0
        second_idx = i
        cnt = 1

        while second_idx < len(s) + i:
            tmp = s[first_idx:second_idx]
            tmp_2 = s[second_idx : second_idx + i]
            if tmp == tmp_2:
                cnt += 1
            else:
                res += (str(cnt) + tmp) if cnt != 1 else tmp
                cnt = 1
            first_idx = second_idx
            second_idx += i

        result.append(len(res))

    return min(result)


# len(s) == 1일때  추가해줬다.
