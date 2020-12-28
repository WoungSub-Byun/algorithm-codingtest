def solution():
    # L1, L2
    move_steps = [[-2, -1], [-2, -1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]

    location = input()
    row = int(location[1])
    column = ord(location[0]) - ord('a') + 1
    count = 0
    for i in move_steps:
        ny = row + i[1]
        nx = column + i[0]
        if ny > 8 or ny < 1 or nx > 8 or nx < 1:
            continue
        else:
            count += 1
    return count
