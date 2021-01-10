# 첫번째 풀이 - 0
from itertools import permutations

def solution(numbers):
    return max([''.join([str(nn) for nn in n]) for n in list(permutations(numbers,len(numbers)))])
# permutations로 모든 조합을 만들어내고 리스트로 바꾸고 각각을 join하고 그 리스트에서 최댓값을 찾아내는... 단순한 풀이법
# 테스트케이스는 맞았지만 시간초과로 0점이었다.    

