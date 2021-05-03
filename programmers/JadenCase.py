# 1차 시도: 43%

# 풀이: 정규식을 통해 첫글자가 숫자인지 판별하였다. 테스트 케이스는 통과하였지만 제출하였더니 많이 틀렸다.
import re


def solution(s):
    answer = [
        word.title() if not re.match("[0-9]", word[0]) else word for word in s.split()
    ]
    return " ".join(answer)
