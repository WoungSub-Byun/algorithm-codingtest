# 첫번쨰 풀이
def solution():
    input_str = list(input())
    char_list = [i for i in input_str if ord(i) >= 64]
    char_list.sort()
    num = sum([int(i) for i in input_str if ord(i) < 64])
    return ''.join(char_list)+str(num)

# 두번쨰 풀이
def solution():
    input_str = list(input())
    num = 0
    result = []
    for i in input_str:
        if i.isalpha():
            result.append(i)
        else:
            num += int(i)
    result.sort()
    return ''.join(result) + str(num)

