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


# 이전 좌표까지 넣었지만 경로의 이동방향에 따라 두가지 경우로 나누지 않기 때문에 현재 좌표에서 이전 좌표로가는 경로도 추가해주어야 한다.
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
        prev = (x, y)
        x += dir[0]
        y += dir[1]
        if x < -5 or x > 5 or y < -5 or y > 5:
            x += -dir[0]
            y += -dir[1]
            continue
        elif [prev, (x, y)] in visited:
            continue
        visited.append([prev, (x, y)])
    return len(visited)


# 최종 제출본
def solution(dirs):

    x, y = 0, 0
    new_dirs, visited = (
        list(),
        list(),
    )  # new_dir: 문자를 이동방향으로 바꾸어준 리스트, visited: 지나간 경로를 확인하기 위한 리스트

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
        prev = (x, y)  # 이전 좌표
        x += dir[0]
        y += dir[1]
        if (
            x < -5 or x > 5 or y < -5 or y > 5
        ):  # 맵의 길이가 (-5, 5)이기 때문에 이를 넘어가게 된다면 이전에 더했던 이동방향을 다시 빼준다.
            x += -dir[0]
            y += -dir[1]
            continue
        elif [prev, (x, y)] in visited or [
            (x, y),
            prev,
        ] in visited:  # 맵을 이탈하지 않았다면 이미 지나간 경로인지 visited리스트를 통해 확인한다.
            continue
        visited.append([prev, (x, y)])  # 위의 두 조건문에 걸리지 않았다면 이동 경로를 visited에 추가해준다.
    return len(visited)


# dictionary와 set을 사용한 간결한 풀이
def solution(dirs):
    visited = set()
    move = {"U": (0, 1), "L": (-1, 0), "D": (0, -1), "R": (1, 0)}
    x, y = 0, 0
    for dir in dirs:
        nx, ny = x + move[dir][0], y + move[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            x, y = nx, ny
    return len(visited) // 2