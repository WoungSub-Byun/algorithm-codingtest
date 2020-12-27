#첫번째 풀이 정확도: 75 효율성 20 => 95
def solution(people, limit):
    rescue = 0
    people.sort()
    r = len(people)
    for i in range(r):
        if people[0] + people[-1] <= limit:
            del people[0]
        people.pop()
        rescue = 1
        if len(people) < 2:
            if len(people) == 0:
                break
            rescue+=1
            break
    return rescue

