# 1차 풀이 100
def solution(n):
    answer = n + 1  # 다음 큰숫자는 n보다 큰 자연수이기 때문에 n+1로 초깃값 세팅
    while True:
        if bin(n).count("1") == bin(answer).count("1"):  # 2진수 값의 1개수 비교
            return answer  # 같으면 return
        answer += 1  # ++


# 2차 풀이 100
def solution(n):
    answer = n + 1
    n = bin(n).count("1")
    while True:
        if n == bin(answer).count("1"):
            return answer
        answer += 1


# 1번 풀이를 보면 answer가 하나 증가할 때마다 2진수값을 비교하는데,
# 이때 n의 2진수값은 바뀌지 않는 상수 값이기 때문에 while문 들어가기 전 n을
# 미리 2진수의 1갯수로 바꾸어 놓아 비교함으로써 연산 실행 수를 줄였다.