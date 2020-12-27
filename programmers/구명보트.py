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

# 두번째 풀이 -> 정답 -> 인덱스를 사용하여 풀어야 한다. del, pop 등을 사용하면 정확도는 맞지만 효율성에서 틀리게 된다.
def solution(people, limit):
    rescue = 0
    people.sort()
    i = 0
    j = len(people) -1
    while i<=j:
        rescue+=1
        if people[i] + people[j] <= limit:
            i+=1
        j-=1
    return rescue
