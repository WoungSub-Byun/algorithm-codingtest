# 첫번째 풀이
def solution(N, M, K):
    data = list(map(int, input().split()))

    data.sort()
    first = data[n-1]
    second = data[n-2]
    answer = []
    while M != 0:
        for i in range(K):
            answer.append(first)
            M -= 1
        answer.append(second)
        M -= 1
    return sum(answer)


# 두번째 풀이
def solution(N, M, K):
    data = list(map(int, input().split()))

    data.sort()
    first = data[n - 1]
    second = data[n - 2]
    first_count = int(M / (K + 1)) * K + M % (K + 1)
    second_count = int(M / (K + 1))
    return first * first_count + second * second_count

n,m,k = map(int, input().split())
print(solution(n,m,k))
