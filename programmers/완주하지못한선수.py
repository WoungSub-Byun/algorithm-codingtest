# 첫번째 풀이 -> 정확성: 100.0 효율성: 0
def solution(participant, completion):
    for row in completion:
        participant.remove(completion)

    return participant[0]


