# 1차 시도: 25%
# 풀이: 방문한 좌표를 visited 리스트에 넣어 중복 여부를 판단했는데, 이렇게 하면 경로가 아닌 방문한 좌표를 기반으로 세어지기 때문에 4개의 경우의 수를 무시한 셈이 된다.
def solution(dirs):
    x, y = 0, 0
    new_dirs, visited = list(), list()
    for dir in dirs:
        if dir == "U":
            new_dirs.append([0, 1])
        elif dir == "L":
            new_dirs.append([-1, 0])
        elif dir == "R":
            new_dirs.append([1, 0])
        elif dir == "D":
            new_dirs.append([0, -1])
    for dir in new_dirs:
        x += dir[0]
        y += dir[1]
        if x < -5 or x > 5 or y < -5 or y > 5:
            x += -dir[0]
            y += -dir[1]
            continue
        elif (x, y) in visited:
            continue
        visited.append((x, y))
    return len(visited)
