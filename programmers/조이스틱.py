# 첫번째 풀이 - 63.6
def solution(name):
    answer = 0
    if len(name) == name.count('A'):
        return 0
    for s in name:
        if 90 - ord(s) > ord(s) - 65:
            answer+= ord(s) - 65
        else:
            answer+= 91 - ord(s)
    right_met = len(name) -1
    turn_met = -1
    check=True
    if 'A' in name:
        for i in range(len(name)):
            if i == len(name)-1:
                if name[i] != 'A':
                    turn_met+=1
                break
            if name[i] == 'A':
                continue
            else:
                if name[i+1] == 'A':
                    if check:
                        turn_met+=i
                        check=False
            turn_met+=1
        
        if turn_met < right_met:
            return answer+turn_met
    return answer+right_met

#두번째 풀이 - 100

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
def solution(name):
    m = [ min(ord(c) - 65, 91-ord(c)) for c in name]       

    answer = 0
    where = 0

    while True:    
        answer += m[where]
        m[where] = 0

        if sum(m) == 0:
            break

        left, right = (1,1)

        while m[where - left] <= 0:
            left += 1
        while m[where + right] <= 0:
            right += 1

        answer += left if left < right else right
        where += -left if left < right else right

    return answer
