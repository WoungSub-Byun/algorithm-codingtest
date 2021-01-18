# 1차 61.5
def solution(brown, yellow):
    if yellow == 1:
        return [3, 3]
    opt = 1 if yellow % 2 == 0 else 3
    for i in range(1, yellow+1, opt):
        width, height = (yellow // i) + 2, i + 2
        if (width * 2) + 2 * (height - 2) == brown:
            return [width, height]