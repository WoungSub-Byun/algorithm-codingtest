# 첫번째 풀이 -> 정확성: 100.0 효율성: 0
def solution(participant, completion):
    for row in completion:
        participant.remove(completion)

    return participant[0]


# 두번째 풀이 -> 정확성: 100 효율성: 100
def solution(participant, completion):
    participant.sort() # O(nlogn)
    completion.sort() # O(nlogn)
    for i, z in zip(participant, completion):
        if i != z:
            return i
    return participant[-1]

# 세번째 풀이 -> 정확성: 100 효율성: 100
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]