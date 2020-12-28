def solution():
    map_size = int(input())
    plan = input().split()
    location = [1,1]
    for i in plan:
        if i == 'R':
            location[1] += 1
        elif i == 'L':
            location[1] -= 1
        elif i == 'U':
            location[0] -= 1
        elif i == 'D':
            location[0] += 1
        if location[0] < 1:
            location[0] += 1
        elif location[0] > map_size:
            location[0] -= 1
        elif location[1] < 1:
            location[1] += 1
        elif location[1] > map_size:
            location[1] -= 1
    print(location)


def solution2():
    map_size = int(input())
    plan = input().split()
    x, y = 1, 1
    nx, ny = 0, 0
    # L, R, U, D
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for i in plan:
        for j in range(len(move_types)):
            if i == move_types[j]:
                nx = x + dx[j]
                ny = y + dy[j]
        if nx < 1 or ny < 1 or nx > map_size or ny > map_size:
            continue
        x, y = nx, ny
    print(x, y)