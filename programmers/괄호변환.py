# 첫번째 풀이 - 100 - 내힘으로 2시간만에 풀었다 기분 너무 좋네
def solution(p):
    if check_right_str(p):
        return p
    return main(p)


def main(p) -> str:
    if len(p) == 0:
        return p
    else:
        u, v = divide_str(p)
        if check_right_str(u):
            v_res = main(v)
            return u + v_res
        else:
            re_v = main(v)
            result = "(" + re_v + ")"

            for i in u[1:-1]:
                if i == "(":
                    result += ")"
                else:
                    result += "("
            return result


def check_right_str(data) -> bool:
    check_dict = {"(": 0, ")": 0}
    for i in data:
        check_dict[i] += 1
        if check_dict[")"] > check_dict["("]:
            return False
    return True


def divide_str(data):
    u = ""
    v = ""
    check_dict = {"(": 0, ")": 0}
    for i in data:
        check_dict[i] += 1
        u += i
        if check_dict["("] == check_dict[")"] and check_dict["("] > 0 and check_dict[")"] > 0:
            return u, data[sum(check_dict.values()):]
