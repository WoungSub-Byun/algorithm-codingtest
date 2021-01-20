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