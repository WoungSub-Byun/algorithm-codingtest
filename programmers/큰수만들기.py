# 첫번째 풀이 Error
def solution(number, k):
    list_number = list(number)
    temp = 0

    min_numbers = list(sorted(list_number))[:k]
    for num in min_numbers:
        list_number.remove(num)
    return int(''.join(list_number))

# 두 번째 풀이 -> Error
def solution(number, k):
    list_number = list(number)
    answer = []
    answer_len = len(list_number) - k
    while answer_len != 0:
        answer.append(max(list_number[:answer_len]))
        list_number.remove(max(list_number[:answer_len]))
        answer_len-=1
    return ''.join(answer)

# 세번째 풀이
def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += number[i:]
            break
        collected.append(num)
    collected = collected[:-k] if k > 0 else collected
    answer = "".join(collected)
    return answer