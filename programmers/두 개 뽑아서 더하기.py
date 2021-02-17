# 첫번째 100
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            try:
                answer.append(numbers[i]+numbers[j])
            except Exception as e:
                break
    answer = sorted(list(set(answer)))
    return answer

