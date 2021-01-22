# 1차 100
def solution(n):
    answer = 1  # 자기자신은 항상 포함하기 때문에 answer의 초깃값을 1로 설정합니다.
    continuous_nums = [0]  # 연속된 숫자들을 저장하는 리스트
    i = 1  #  temp에 들어가는 수 - 0은 더해도 아무런 변화가 일어나지 않기 때문에 초깃값을 1로 설정합니다.
    while i < n:
        continuous_nums.append(i)
        if sum(temp) == n:  # 숫자들의 합이 n이라면
            answer += 1  # answer에 1을 더해줍니다
            i = min(temp)  #  가장 하단에 i+=1이 있기 때문에 i를 리스트의 최솟값으로 바꿔줍니다.
            temp = []  # 리스트를 비워줍니다
        if sum(temp) > n:  # 리스트의 합이 n보다 크다면 해당 연속된 숫자 조합은 n이 될 수 없습니다.
            i = min(temp)
            temp = []
        i += 1

    return answer
