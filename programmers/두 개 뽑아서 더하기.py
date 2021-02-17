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

# 두번째 풀이

from itertools import combinations

def solution(numbers):
    numbers = list(combinations(numbers, 2))
    
    answer = list(set([i[0]+i[1] for i in numbers]))
    answer.sort()
    return answer
    