# 첫번째 풀이 - 100 (문제 이해하고 처음 쓴 코드가 맞아버렸다...)
def solution(skill, skill_trees):
    skill_trees = [ [j for j in i if j in skill] for i in skill_trees ]
    answer=0
    for skill_tree in skill_trees:
        count = 0
        for j in skill_tree:
            if j == skill[count]:
                count+=1
            else:
                break
        if count == len(skill_tree):
            answer+=1
    
    return answer

